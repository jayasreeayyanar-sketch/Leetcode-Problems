class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        # Track the coordinates of the overall bounding box
        X1, Y1 = float('inf'), float('inf')
        X2, Y2 = float('-inf'), float('-inf')
        
        total_area = 0
        corners = set()
        
        for x1, y1, x2, y2 in rectangles:
            # Update the global bounding box
            X1 = min(X1, x1)
            Y1 = min(Y1, y1)
            X2 = max(X2, x2)
            Y2 = max(Y2, y2)
            
            # Accumulate individual area
            total_area += (x2 - x1) * (y2 - y1)
            
            # Process the 4 corners of the current rectangle
            # If a corner is already in the set, they cancel out (remove it)
            # If it's not, we add it. This leaves only corners with odd counts.
            for corner in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)
                    
        # Condition 1: Check if the final set has exactly the 4 outermost corners
        expected_corners = {(X1, Y1), (X1, Y2), (X2, Y1), (X2, Y2)}
        if corners != expected_corners:
            return False
            
        # Condition 2: Check if the sum of individual areas matches the large bounding box area
        return total_area == (X2 - X1) * (Y2 - Y1)


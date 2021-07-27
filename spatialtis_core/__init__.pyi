from typing import List, Tuple, Dict, Optional

import numpy as np

Points = List[Tuple[float, float]]
BoundingBox = Tuple[float, float, float, float]
Neighbors = List[List[int]]
Labels = List[int]


def multi_points_bbox(points: Points) -> BoundingBox:
    """Return minimum bounding box of a list of points

    Args:
        points: A list of points

    Return:
        The bounding box (minx, miny, maxx, maxy)

    """
    ...


def points2bbox(points_collections: List[Points]) -> List[BoundingBox]:
    """
    points2bbox(points_collections)
    --

    A utility function to return minimum bounding box list of polygons

    Args:
        points_collections: List of 2d points collections

    Return:
        A list of bounding box (minx, miny, maxx, maxy)

    """
    ...


def points2shapes(p: Points, method: str = "convex", concavity: float = 1.5) -> Points:
    """Acquire multipoints (shapes) that describe the points

    Args:
        p: A list of points
        method: "convex" or "concave"
        concavity: Determine the concavity in concave hull

    Return:
        A list of points

    """
    ...


def points_neighbors(points: Points,
                     labels: Optional[Labels] = None,
                     r: Optional[float] = None,
                     k: Optional[int] = None,
                     method: str = "kdtree",
                     ) -> List[List[int]]:
    """Get neighbors for each points

    When search with KD-tree, you can use either `r` or `k`.
    If r = 5, it will search for all points within 5; If k = 5, it will
    search for the 5 nearest neighbors; If combined, r = 5 and k = 5, it will
    search for at most 5 neighbors within 5;

    When search with Delaunay triangulation, there is no parameter.

    The return list follow the order of labels. For example, if serach for points of
    [100, 101, 102], the result may look like [[100, 102], [101, 102], [102, 100, 101]]

    Args:
        points: A list of points
        labels: Integer to labels your points
        r: Radius range to search for neighbors
        k: Number of nearest neighbors
        method: "kdtree" or "delaunay"

    Return:
         A list of neighbors

    """
    ...


def bbox_neighbors(bbox: List[BoundingBox],
                   labels: Optional[Labels] = None,
                   expand: Optional[float] = None,
                   scale: Optional[float] = 1.3,
                   ) -> List[List[int]]:
    """Get neighbors for each bouding box

    Args:
        bbox: A list of bounding box
        labels: Integer to labels your bounding box
        expand: Expand the bounding box to search for neighbors
        scale: Scale the bounding box to search for neighbors

    Return:
        A list of neighbors

    """
    ...


def neighbor_components(neighbors: Dict[int, List[int]], types: Dict[int, str],
                        ) -> (List[int], List[str], List[List[int]]):
    """Compute the number of different cells at neighbors

    Args:
        neighbors: The neighbors dict
        types: The

    :param neighbors:
    :param types:
    :return:
    """
    ...


def spatial_autocorr(x: np.ndarray,
                     neighbors: Neighbors,
                     labels: Labels,
                     two_tailed: bool = True,
                     method: str = "moran_i") -> List[Tuple[float, float]]:
    """Compute spatial auto-correlation value for a 2D array in parallel

    The p-value is under the assumption of normal distribution
    Return is tuples of (spatial_autocorr value, p value)

    Args:
        x: Gene expression matrix, each row is the expression of a gene
        neighbors: A list of neighbors
        labels: A list of labels
        two_tailed: Determine the p value
        method: "moran_i" or "geary_c"

    Return:
        A list of (value, p_value)

    """
    ...


def spatial_distribution_pattern(points_collections: List[Points],
                                 bbox: BoundingBox,
                                 method: str = "id",
                                 r: Optional[float] = None,
                                 resample: int = 1000,
                                 quad: Optional[Tuple[int, int]] = None,
                                 rect_side: Optional[Tuple[float, float]] = None,
                                 pval: float = 0.05,
                                 min_cells: int = 10,
                                 ) -> List[Tuple[float, float, int]]:
    """Compute the distribution index and determine the pattern for different cells in a ROI in parallel

    Args:
        points_collections: A list of list of points
        bbox: The bounding box
        method: "id" for index of dispersion, "morisita" for morisita index, "clark_evans" for clark evans' index
        r: If method == "id"; The sample windows' radius
        resample: If method == "id"; The number of sampling times
        quad: If method == "morisita"; eg.(X, Y) Use X * Y grid to perform analysis
        rect_side: If method == "morisita"; eg.(X, Y) Use X * Y rectangle to perform analysis
        pval: The threshold for p-value
        min_cells: The minimum number of cells to perform analysis

    Return:
        A list of (index_value, p_value, pattern)

    """
    ...


def spatial_entropy(points_collections: List[Points],
                    types_collections: List[List[int]],
                    method: str = "leibovici",
                    d: Optional[float] = None,
                    cut: int = 3,
                    order: bool = False,
                    ) -> List[float]:
    """Compute spatial entropy value of multiple ROIs in parallel

    Args:
        points_collections: A list of list of points
        types_collections: A list of list of types
        bbox: The bounding box
        method: "leibovici" or "altieri"
        d: If method == "leibovici"; The distance threshold to determine co-occurrence
        cut: If method == "altieri"; The distance interval to determine co-occurrence
        order: If order == False, (A, B) and (B, A) is the same

    Return:
        A list of spatial entropy

    """
    ...


def getis_ord(points: Points,
              bbox: BoundingBox,
              search_level: int = 3,
              quad: Optional[Tuple[int, int]] = None,
              rect_side: Optional[Tuple[float, float]] = None,
              pval: float = 0.05,
              min_cells: int = 10,
              ) -> List[bool]:
    """Getis-ord analysis to find hot cells

    Args:
        points: A list of points
        bbox: The bounding box
        search_level: The level of outer-ring to search for
        quad: eg.(X, Y) Use X * Y grid to perform analysis
        rect_side: eg.(X, Y) Use X * Y rectangle to perform analysis
        pval: The threshold for p-value
        min_cells: The minimum number of cells to perform analysis

    Return:
        A list of bool

    """
    ...


def comb_bootstrap(x_status: List[bool], y_status: List[bool], neighbors: Neighbors,
                   labels: Labels, times: int = 1000, ignore_self: bool = False) -> float:
    """
    Bootstrap between two types

    If you want to test co-localization between protein X and Y, first determine if the cell is X-positive
    and/or Y-positive. True is considered as positive and will be counted.

    Args:
        x_status: If cell is type x
        y_status: If cell is type y
        neighbors: List of neighbors
        labels: List of labels
        times: How many times to perform bootstrap
        ignore_self: Whether to consider self as a neighbor

    Return:
        The p-value for the spatial relationship between X and Y

    """
    ...


class CellCombs:
    """Profile cell-cell interaction using permutation test

    Args:
        types: All the type of cells in your research
        order: bool (False); If False, A->B and A<-B is the same

    """

    def __init__(self, types: List[str], order: bool = False): ...

    def bootstrap(self, types: List[str], neighbors: Neighbors, labels: Labels, times: int = 1000, pval: float = 0.05,
                  method: str = 'pval', ignore_self: bool = False) -> List[Tuple[Tuple[str, str], float]]:
        """
        Bootstrap functions

        1.0 means association, -1.0 means avoidance, 0.0 means insignificance.

        Args:
            types: The type of all the cells
            neighbors: List of neighbors
            labels: List of labels
            times: How many times to perform bootstrap
            pval: The threshold of p-value
            method: 'pval' or 'zscore'
            ignore_self: Whether to consider self as a neighbor

        Return:
            List of tuples, eg.(('a', 'b'), 1.0), the type a and type b has a relationship as association

        """
        ...

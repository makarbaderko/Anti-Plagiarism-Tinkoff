Module(body=[ImportFrom(module='typing', names=[alias(name='TYPE_CHECKING')], level=0), ImportFrom(module='typing', names=[alias(name='Callable')], level=0), ImportFrom(module='typing', names=[alias(name='Dict')], level=0), ImportFrom(module='typing', names=[alias(name='List')], level=0), Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pandas', asname='pd')]), If(test=Name(id='TYPE_CHECKING', ctx=Load()), body=[ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0)], orelse=[]), FunctionDef(name='absolute_difference_distance', args=arguments(posonlyargs=[], args=[arg(arg='x', annotation=Name(id='float', ctx=Load())), arg(arg='y', annotation=Name(id='float', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Calculate distance for :py:func:`get_anomalies_density` function by taking absolute value of difference.\n\n    Parameters\n    ----------\n    x:\n        first value\n    y:\n        second value\n\n    Returns\n    -------\n    result: float\n        absolute difference between values\n    ')), Return(value=Call(func=Name(id='abs', ctx=Load()), args=[BinOp(left=Name(id='x', ctx=Load()), op=Sub(), right=Name(id='y', ctx=Load()))], keywords=[]))], decorator_list=[], returns=Name(id='float', ctx=Load())), FunctionDef(name='get_segment_density_outliers_indices', args=arguments(posonlyargs=[], args=[arg(arg='series', annotation=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load())), arg(arg='window_size', annotation=Name(id='int', ctx=Load())), arg(arg='distance_threshold', annotation=Name(id='float', ctx=Load())), arg(arg='n_neighbors', annotation=Name(id='int', ctx=Load())), arg(arg='distance_func', annotation=Subscript(value=Name(id='Callable', ctx=Load()), slice=Tuple(elts=[List(elts=[Name(id='float', ctx=Load()), Name(id='float', ctx=Load())], ctx=Load()), Name(id='float', ctx=Load())], ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=7), Constant(value=10), Constant(value=3), Name(id='absolute_difference_distance', ctx=Load())]), body=[Expr(value=Constant(value="Get indices of outliers for one series.\n\n    Parameters\n    ----------\n    series:\n        array to find outliers in\n    window_size:\n        size of window\n    distance_threshold:\n        if distance between two items in the window is less than threshold those items are supposed to be close to each other\n    n_neighbors:\n        min number of close items that item should have not to be outlier\n    distance_func:\n        distance function\n\n    Returns\n    -------\n    :\n        list of outliers' indices\n    ")), FunctionDef(name='is_close', args=arguments(posonlyargs=[], args=[arg(arg='item1', annotation=Name(id='float', ctx=Load())), arg(arg='item2', annotation=Name(id='float', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Return 1 if item1 is closer to item2 than distance_threshold according to distance_func, 0 otherwise.')), Return(value=Call(func=Name(id='int', ctx=Load()), args=[Compare(left=Call(func=Name(id='distance_func', ctx=Load()), args=[Name(id='item1', ctx=Load()), Name(id='item2', ctx=Load())], keywords=[]), ops=[Lt()], comparators=[Name(id='distance_threshold', ctx=Load())])], keywords=[]))], decorator_list=[], returns=Name(id='int', ctx=Load())), Assign(targets=[Name(id='outliers_indices', ctx=Store())], value=List(elts=[], ctx=Load())), For(target=Tuple(elts=[Name(id='idx', ctx=Store()), Name(id='item', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='enumerate', ctx=Load()), args=[Name(id='series', ctx=Load())], keywords=[]), body=[Assign(targets=[Name(id='is_outlier', ctx=Store())], value=Constant(value=True)), Assign(targets=[Name(id='left_start', ctx=Store())], value=Call(func=Name(id='max', ctx=Load()), args=[Constant(value=0), BinOp(left=Name(id='idx', ctx=Load()), op=Sub(), right=Name(id='window_size', ctx=Load()))], keywords=[])), Assign(targets=[Name(id='left_stop', ctx=Store())], value=Call(func=Name(id='max', ctx=Load()), args=[Constant(value=0), Call(func=Name(id='min', ctx=Load()), args=[Name(id='idx', ctx=Load()), BinOp(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='series', ctx=Load())], keywords=[]), op=Sub(), right=Name(id='window_size', ctx=Load()))], keywords=[])], keywords=[])), Assign(targets=[Name(id='closeness', ctx=Store())], value=Constant(value=None)), Assign(targets=[Name(id='n', ctx=Store())], value=Constant(value=0)), For(target=Name(id='i', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='left_start', ctx=Load()), BinOp(left=Name(id='left_stop', ctx=Load()), op=Add(), right=Constant(value=1))], keywords=[]), body=[If(test=Compare(left=Name(id='closeness', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Assign(targets=[Name(id='closeness', ctx=Store())], value=ListComp(elt=Call(func=Name(id='is_close', ctx=Load()), args=[Name(id='item', ctx=Load()), Subscript(value=Name(id='series', ctx=Load()), slice=Name(id='j', ctx=Load()), ctx=Load())], keywords=[]), generators=[comprehension(target=Name(id='j', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='i', ctx=Load()), Call(func=Name(id='min', ctx=Load()), args=[BinOp(left=Name(id='i', ctx=Load()), op=Add(), right=Name(id='window_size', ctx=Load())), Call(func=Name(id='len', ctx=Load()), args=[Name(id='series', ctx=Load())], keywords=[])], keywords=[])], keywords=[]), ifs=[], is_async=0)])), Assign(targets=[Name(id='n', ctx=Store())], value=BinOp(left=Call(func=Name(id='sum', ctx=Load()), args=[Name(id='closeness', ctx=Load())], keywords=[]), op=Sub(), right=Constant(value=1)))], orelse=[AugAssign(target=Name(id='n', ctx=Store()), op=Sub(), value=Call(func=Attribute(value=Name(id='closeness', ctx=Load()), attr='pop', ctx=Load()), args=[Constant(value=0)], keywords=[])), Assign(targets=[Name(id='new_element_is_close', ctx=Store())], value=Call(func=Name(id='is_close', ctx=Load()), args=[Name(id='item', ctx=Load()), Subscript(value=Name(id='series', ctx=Load()), slice=BinOp(left=BinOp(left=Name(id='i', ctx=Load()), op=Add(), right=Name(id='window_size', ctx=Load())), op=Sub(), right=Constant(value=1)), ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='closeness', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='new_element_is_close', ctx=Load())], keywords=[])), AugAssign(target=Name(id='n', ctx=Store()), op=Add(), value=Name(id='new_element_is_close', ctx=Load()))]), If(test=Compare(left=Name(id='n', ctx=Load()), ops=[GtE()], comparators=[Name(id='n_neighbors', ctx=Load())]), body=[Assign(targets=[Name(id='is_outlier', ctx=Store())], value=Constant(value=False)), Break()], orelse=[])], orelse=[]), If(test=Name(id='is_outlier', ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Name(id='outliers_indices', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='idx', ctx=Load())], keywords=[]))], orelse=[])], orelse=[]), Return(value=Call(func=Name(id='list', ctx=Load()), args=[Name(id='outliers_indices', ctx=Load())], keywords=[]))], decorator_list=[], returns=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='int', ctx=Load()), ctx=Load())), FunctionDef(name='get_anomalies_density', args=arguments(posonlyargs=[], args=[arg(arg='ts', annotation=Constant(value='TSDataset')), arg(arg='in_column', annotation=Name(id='str', ctx=Load())), arg(arg='window_size', annotation=Name(id='int', ctx=Load())), arg(arg='distance_coef', annotation=Name(id='float', ctx=Load())), arg(arg='n_neighbors', annotation=Name(id='int', ctx=Load())), arg(arg='distance_func', annotation=Subscript(value=Name(id='Callable', ctx=Load()), slice=Tuple(elts=[List(elts=[Name(id='float', ctx=Load()), Name(id='float', ctx=Load())], ctx=Load()), Name(id='float', ctx=Load())], ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value='target'), Constant(value=15), Constant(value=3), Constant(value=3), Name(id='absolute_difference_distance', ctx=Load())]), body=[Expr(value=Constant(value='Compute outliers according to density rule.\n\n    For each element in the series build all the windows of size ``window_size`` containing this point.\n    If any of the windows contains at least ``n_neighbors`` that are closer than ``distance_coef * std(series)``\n    to target point according to ``distance_func`` target point is not an outlier.\n\n    Parameters\n    ----------\n    ts:\n        TSDataset with timeseries data\n    in_column:\n        name of the column in which the anomaly is searching\n    window_size:\n        size of windows to build\n    distance_coef:\n        factor for standard deviation that forms distance threshold to determine points are close to each other\n    n_neighbors:\n        min number of close neighbors of point not to be outlier\n    distance_func:\n        distance function\n\n    Returns\n    -------\n    :\n        dict of outliers in format {segment: [outliers_timestamps]}\n\n    Notes\n    -----\n    It is a variation of distance-based (index) outlier detection method adopted for timeseries.\n    ')), Assign(targets=[Name(id='segments', ctx=Store())], value=Attribute(value=Name(id='ts', ctx=Load()), attr='segments', ctx=Load())), Assign(targets=[Name(id='outliers_per_segment', ctx=Store())], value=Dict(keys=[], values=[])), For(target=Name(id='seg', ctx=Store()), iter=Name(id='segments', ctx=Load()), body=[Assign(targets=[Name(id='segment_df', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Subscript(value=Subscript(value=Name(id='ts', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='seg', ctx=Load()), Slice()], ctx=Load()), ctx=Load()), slice=Name(id='seg', ctx=Load()), ctx=Load()), attr='dropna', ctx=Load()), args=[], keywords=[]), attr='reset_index', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='series', ctx=Store())], value=Attribute(value=Subscript(value=Name(id='segment_df', ctx=Load()), slice=Name(id='in_column', ctx=Load()), ctx=Load()), attr='values', ctx=Load())), Assign(targets=[Name(id='timestamps', ctx=Store())], value=Attribute(value=Subscript(value=Name(id='segment_df', ctx=Load()), slice=Constant(value='timestamp'), ctx=Load()), attr='values', ctx=Load())), Assign(targets=[Name(id='series_std', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='std', ctx=Load()), args=[Name(id='series', ctx=Load())], keywords=[])), If(test=Name(id='series_std', ctx=Load()), body=[Assign(targets=[Name(id='outliers_idxs', ctx=Store())], value=Call(func=Name(id='get_segment_density_outliers_indices', ctx=Load()), args=[], keywords=[keyword(arg='series', value=Name(id='series', ctx=Load())), keyword(arg='window_size', value=Name(id='window_size', ctx=Load())), keyword(arg='distance_threshold', value=BinOp(left=Name(id='distance_coef', ctx=Load()), op=Mult(), right=Name(id='series_std', ctx=Load()))), keyword(arg='n_neighbors', value=Name(id='n_neighbors', ctx=Load())), keyword(arg='distance_func', value=Name(id='distance_func', ctx=Load()))])), Assign(targets=[Name(id='outliers', ctx=Store())], value=ListComp(elt=Subscript(value=Name(id='timestamps', ctx=Load()), slice=Name(id='i', ctx=Load()), ctx=Load()), generators=[comprehension(target=Name(id='i', ctx=Store()), iter=Name(id='outliers_idxs', ctx=Load()), ifs=[], is_async=0)])), Assign(targets=[Subscript(value=Name(id='outliers_per_segment', ctx=Load()), slice=Name(id='seg', ctx=Load()), ctx=Store())], value=Name(id='outliers', ctx=Load()))], orelse=[Assign(targets=[Subscript(value=Name(id='outliers_per_segment', ctx=Load()), slice=Name(id='seg', ctx=Load()), ctx=Store())], value=List(elts=[], ctx=Load()))])], orelse=[]), Return(value=Name(id='outliers_per_segment', ctx=Load()))], decorator_list=[], returns=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Subscript(value=Name(id='List', ctx=Load()), slice=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())), Assign(targets=[Name(id='__all__', ctx=Store())], value=List(elts=[Constant(value='get_anomalies_density'), Constant(value='absolute_difference_distance')], ctx=Load()))], type_ignores=[])
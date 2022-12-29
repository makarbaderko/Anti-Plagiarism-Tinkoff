Module(body=[ImportFrom(module='enum', names=[alias(name='Enum')], level=0), ImportFrom(module='typing', names=[alias(name='Dict')], level=0), ImportFrom(module='typing', names=[alias(name='Tuple')], level=0), ImportFrom(module='typing', names=[alias(name='Union')], level=0), Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='ruptures.base', names=[alias(name='BaseEstimator')], level=0), ImportFrom(module='ruptures.costs', names=[alias(name='CostLinear')], level=0), ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0), ClassDef(name='OptimizationMode', bases=[Name(id='str', ctx=Load()), Name(id='Enum', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Enum for different optimization modes.')), Assign(targets=[Name(id='pen', ctx=Store())], value=Constant(value='pen')), Assign(targets=[Name(id='epsilon', ctx=Store())], value=Constant(value='epsilon')), FunctionDef(name='_missing_', args=arguments(posonlyargs=[], args=[arg(arg='cls'), arg(arg='value')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Raise(exc=Call(func=Name(id='NotImplementedError', ctx=Load()), args=[JoinedStr(values=[FormattedValue(value=Name(id='value', ctx=Load()), conversion=-1), Constant(value=' is not a valid '), FormattedValue(value=Attribute(value=Name(id='cls', ctx=Load()), attr='__name__', ctx=Load()), conversion=-1), Constant(value='. Only '), FormattedValue(value=Call(func=Attribute(value=Constant(value=', '), attr='join', ctx=Load()), args=[ListComp(elt=Call(func=Name(id='repr', ctx=Load()), args=[Attribute(value=Name(id='m', ctx=Load()), attr='value', ctx=Load())], keywords=[]), generators=[comprehension(target=Name(id='m', ctx=Store()), iter=Name(id='cls', ctx=Load()), ifs=[], is_async=0)])], keywords=[]), conversion=-1), Constant(value=' modes allowed')])], keywords=[]))], decorator_list=[Name(id='classmethod', ctx=Load())])], decorator_list=[]), FunctionDef(name='_get_n_bkps', args=arguments(posonlyargs=[], args=[arg(arg='series', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='Series', ctx=Load())), arg(arg='change_point_model', annotation=Name(id='BaseEstimator', ctx=Load()))], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='model_predict_params'), defaults=[]), body=[Expr(value=Constant(value='Get number of change points, detected with given params.\n\n    Parameters\n    ----------\n    series:\n        series to detect change points\n    change_point_model:\n        model to get trend change points\n\n    Returns\n    -------\n    :\n        number of change points\n    ')), Assign(targets=[Name(id='signal', ctx=Store())], value=Call(func=Attribute(value=Name(id='series', ctx=Load()), attr='to_numpy', ctx=Load()), args=[], keywords=[])), If(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Attribute(value=Name(id='change_point_model', ctx=Load()), attr='cost', ctx=Load()), Name(id='CostLinear', ctx=Load())], keywords=[]), body=[Assign(targets=[Name(id='signal', ctx=Store())], value=Call(func=Attribute(value=Name(id='signal', ctx=Load()), attr='reshape', ctx=Load()), args=[Tuple(elts=[UnaryOp(op=USub(), operand=Constant(value=1)), Constant(value=1)], ctx=Load())], keywords=[]))], orelse=[]), Expr(value=Call(func=Attribute(value=Name(id='change_point_model', ctx=Load()), attr='fit', ctx=Load()), args=[], keywords=[keyword(arg='signal', value=Name(id='signal', ctx=Load()))])), Assign(targets=[Name(id='change_points_indices', ctx=Store())], value=Subscript(value=Call(func=Attribute(value=Name(id='change_point_model', ctx=Load()), attr='predict', ctx=Load()), args=[], keywords=[keyword(value=Name(id='model_predict_params', ctx=Load()))]), slice=Slice(upper=UnaryOp(op=USub(), operand=Constant(value=1))), ctx=Load())), Return(value=Call(func=Name(id='len', ctx=Load()), args=[Name(id='change_points_indices', ctx=Load())], keywords=[]))], decorator_list=[], returns=Name(id='int', ctx=Load())), FunctionDef(name='_get_next_value', args=arguments(posonlyargs=[], args=[arg(arg='now_value', annotation=Name(id='float', ctx=Load())), arg(arg='lower_bound', annotation=Name(id='float', ctx=Load())), arg(arg='upper_bound', annotation=Name(id='float', ctx=Load())), arg(arg='need_greater', annotation=Name(id='bool', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Give next value according to binary search.\n\n    Parameters\n    ----------\n    now_value:\n        current value\n    lower_bound:\n        lower bound for search\n    upper_bound:\n        upper bound for search\n    need_greater:\n        True if we need greater value for n_bkps than previous time\n\n    Returns\n    -------\n    :\n        next value and its bounds\n    ')), If(test=Name(id='need_greater', ctx=Load()), body=[Return(value=Tuple(elts=[Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='mean', ctx=Load()), args=[List(elts=[Name(id='now_value', ctx=Load()), Name(id='lower_bound', ctx=Load())], ctx=Load())], keywords=[]), Name(id='lower_bound', ctx=Load()), Name(id='now_value', ctx=Load())], ctx=Load()))], orelse=[Return(value=Tuple(elts=[Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='mean', ctx=Load()), args=[List(elts=[Name(id='now_value', ctx=Load()), Name(id='upper_bound', ctx=Load())], ctx=Load())], keywords=[]), Name(id='now_value', ctx=Load()), Name(id='upper_bound', ctx=Load())], ctx=Load()))])], decorator_list=[], returns=Subscript(value=Name(id='Tuple', ctx=Load()), slice=Tuple(elts=[Name(id='float', ctx=Load()), Name(id='float', ctx=Load()), Name(id='float', ctx=Load())], ctx=Load()), ctx=Load())), FunctionDef(name='bin_search', args=arguments(posonlyargs=[], args=[arg(arg='series', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='Series', ctx=Load())), arg(arg='change_point_model', annotation=Name(id='BaseEstimator', ctx=Load())), arg(arg='n_bkps', annotation=Name(id='int', ctx=Load())), arg(arg='opt_param', annotation=Name(id='str', ctx=Load())), arg(arg='max_value', annotation=Name(id='float', ctx=Load())), arg(arg='max_iters', annotation=Name(id='int', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=200)]), body=[Expr(value=Constant(value='Run binary search for optimal regularizations.\n\n    Parameters\n    ----------\n    series:\n        series for search\n    change_point_model:\n        model to get trend change points\n    n_bkps:\n        target numbers of changepoints\n    opt_param:\n        parameter for optimization\n    max_value:\n        maximum possible value, the upper bound for search\n    max_iters:\n        maximum iterations; in case if the required number of points is unattainable, values will be selected after max_iters iterations\n\n    Returns\n    -------\n    :\n        regularization parameters value\n\n    Raises\n    ______\n    ValueError:\n        If max_value is too low for needed n_bkps\n    ValueError:\n        If n_bkps is too high for this series\n    ')), Assign(targets=[Name(id='zero_param', ctx=Store())], value=Call(func=Name(id='_get_n_bkps', ctx=Load()), args=[Name(id='series', ctx=Load()), Name(id='change_point_model', ctx=Load())], keywords=[keyword(value=Dict(keys=[Name(id='opt_param', ctx=Load())], values=[Constant(value=0)]))])), Assign(targets=[Name(id='max_param', ctx=Store())], value=Call(func=Name(id='_get_n_bkps', ctx=Load()), args=[Name(id='series', ctx=Load()), Name(id='change_point_model', ctx=Load())], keywords=[keyword(value=Dict(keys=[Name(id='opt_param', ctx=Load())], values=[Name(id='max_value', ctx=Load())]))])), If(test=Compare(left=Name(id='zero_param', ctx=Load()), ops=[Lt()], comparators=[Name(id='n_bkps', ctx=Load())]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Impossible number of changepoints. Please, decrease n_bkps value.')], keywords=[]))], orelse=[]), If(test=Compare(left=Name(id='n_bkps', ctx=Load()), ops=[Lt()], comparators=[Name(id='max_param', ctx=Load())]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Impossible number of changepoints. Please, increase max_value or increase n_bkps value.')], keywords=[]))], orelse=[]), Assign(targets=[Tuple(elts=[Name(id='lower_bound', ctx=Store()), Name(id='upper_bound', ctx=Store())], ctx=Store())], value=Tuple(elts=[Constant(value=0.0), Name(id='max_value', ctx=Load())], ctx=Load())), Assign(targets=[Name(id='now_value', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='mean', ctx=Load()), args=[List(elts=[Name(id='lower_bound', ctx=Load()), Name(id='upper_bound', ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='now_n_bkps', ctx=Store())], value=Call(func=Name(id='_get_n_bkps', ctx=Load()), args=[Name(id='series', ctx=Load()), Name(id='change_point_model', ctx=Load())], keywords=[keyword(value=Dict(keys=[Name(id='opt_param', ctx=Load())], values=[Name(id='now_value', ctx=Load())]))])), Assign(targets=[Name(id='iters', ctx=Store())], value=Constant(value=0)), While(test=BoolOp(op=And(), values=[Compare(left=Name(id='now_n_bkps', ctx=Load()), ops=[NotEq()], comparators=[Name(id='n_bkps', ctx=Load())]), Compare(left=Name(id='iters', ctx=Load()), ops=[Lt()], comparators=[Name(id='max_iters', ctx=Load())])]), body=[Assign(targets=[Name(id='need_greater', ctx=Store())], value=Compare(left=Name(id='now_n_bkps', ctx=Load()), ops=[Lt()], comparators=[Name(id='n_bkps', ctx=Load())])), Assign(targets=[Tuple(elts=[Name(id='now_value', ctx=Store()), Name(id='lower_bound', ctx=Store()), Name(id='upper_bound', ctx=Store())], ctx=Store())], value=Call(func=Name(id='_get_next_value', ctx=Load()), args=[Name(id='now_value', ctx=Load()), Name(id='lower_bound', ctx=Load()), Name(id='upper_bound', ctx=Load()), Name(id='need_greater', ctx=Load())], keywords=[])), Assign(targets=[Name(id='now_n_bkps', ctx=Store())], value=Call(func=Name(id='_get_n_bkps', ctx=Load()), args=[Name(id='series', ctx=Load()), Name(id='change_point_model', ctx=Load())], keywords=[keyword(value=Dict(keys=[Name(id='opt_param', ctx=Load())], values=[Name(id='now_value', ctx=Load())]))])), AugAssign(target=Name(id='iters', ctx=Store()), op=Add(), value=Constant(value=1))], orelse=[]), Return(value=Name(id='now_value', ctx=Load()))], decorator_list=[], returns=Name(id='float', ctx=Load())), FunctionDef(name='get_ruptures_regularization', args=arguments(posonlyargs=[], args=[arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load())), arg(arg='in_column', annotation=Name(id='str', ctx=Load())), arg(arg='change_point_model', annotation=Name(id='BaseEstimator', ctx=Load())), arg(arg='n_bkps', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='int', ctx=Load())], ctx=Load()), ctx=Load()), Name(id='int', ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='mode', annotation=Name(id='OptimizationMode', ctx=Load())), arg(arg='max_value', annotation=Name(id='float', ctx=Load())), arg(arg='max_iters', annotation=Name(id='int', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=10000), Constant(value=200)]), body=[Expr(value=Constant(value='Get regularization parameter values for given number of changepoints.\n\n    It is assumed that as the regularization being selected increases, the number of change points decreases.\n\n    Parameters\n    ----------\n    ts:\n        Dataset with timeseries data\n    in_column:\n        name of processed column\n    change_point_model:\n        model to get trend change points\n    n_bkps:\n        target numbers of changepoints\n    mode:\n        optimization mode\n    max_value:\n        maximum possible value, the upper bound for search\n    max_iters:\n        maximum iterations; in case if the required number of points is unattainable, values will be selected after max_iters iterations\n\n    Returns\n    -------\n    :\n        regularization parameters values in dictionary format {segment: {mode: value}}.\n\n    Raises\n    ______\n    ValueError:\n        If max_value is too low for needed n_bkps\n    ValueError:\n        If n_bkps is too high for this series\n    ')), Assign(targets=[Name(id='mode', ctx=Store())], value=Call(func=Name(id='OptimizationMode', ctx=Load()), args=[Name(id='mode', ctx=Load())], keywords=[])), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='to_pandas', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='segments', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value=0)], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[])), If(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='n_bkps', ctx=Load()), Name(id='int', ctx=Load())], keywords=[]), body=[Assign(targets=[Name(id='n_bkps', ctx=Store())], value=Call(func=Name(id='dict', ctx=Load()), args=[Call(func=Name(id='zip', ctx=Load()), args=[Name(id='segments', ctx=Load()), BinOp(left=List(elts=[Name(id='n_bkps', ctx=Load())], ctx=Load()), op=Mult(), right=Call(func=Name(id='len', ctx=Load()), args=[Name(id='segments', ctx=Load())], keywords=[]))], keywords=[])], keywords=[]))], orelse=[]), Assign(targets=[Name(id='regulatization', ctx=Store())], value=Dict(keys=[], values=[])), For(target=Name(id='segment', ctx=Store()), iter=Name(id='segments', ctx=Load()), body=[Assign(targets=[Name(id='series', ctx=Store())], value=Subscript(value=Name(id='ts', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='segment', ctx=Load()), Name(id='in_column', ctx=Load())], ctx=Load()), ctx=Load())), Assign(targets=[Subscript(value=Name(id='regulatization', ctx=Load()), slice=Name(id='segment', ctx=Load()), ctx=Store())], value=Dict(keys=[Attribute(value=Name(id='mode', ctx=Load()), attr='value', ctx=Load())], values=[Call(func=Name(id='bin_search', ctx=Load()), args=[Name(id='series', ctx=Load()), Name(id='change_point_model', ctx=Load()), Subscript(value=Name(id='n_bkps', ctx=Load()), slice=Name(id='segment', ctx=Load()), ctx=Load()), Name(id='mode', ctx=Load()), Name(id='max_value', ctx=Load()), Name(id='max_iters', ctx=Load())], keywords=[])]))], orelse=[]), Return(value=Name(id='regulatization', ctx=Load()))], decorator_list=[], returns=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='float', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()))], type_ignores=[])
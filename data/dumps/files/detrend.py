Module(body=[Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='sklearn.base', names=[alias(name='RegressorMixin')], level=0), ImportFrom(module='sklearn.linear_model', names=[alias(name='LinearRegression')], level=0), ImportFrom(module='sklearn.linear_model', names=[alias(name='TheilSenRegressor')], level=0), ImportFrom(module='sklearn.pipeline', names=[alias(name='Pipeline')], level=0), ImportFrom(module='sklearn.preprocessing', names=[alias(name='PolynomialFeatures')], level=0), ImportFrom(module='etna.transforms.base', names=[alias(name='PerSegmentWrapper')], level=0), ImportFrom(module='etna.transforms.base', names=[alias(name='Transform')], level=0), ImportFrom(module='etna.transforms.utils', names=[alias(name='match_target_quantiles')], level=0), ClassDef(name='_OneSegmentLinearTrendBaseTransform', bases=[Name(id='Transform', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='LinearTrendBaseTransform is a base class that implements trend subtraction and reconstruction feature.')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='in_column', annotation=Name(id='str', ctx=Load())), arg(arg='regressor', annotation=Name(id='RegressorMixin', ctx=Load())), arg(arg='poly_degree', annotation=Name(id='int', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=1)]), body=[Expr(value=Constant(value='\n        Create instance of _OneSegmentLinearTrendBaseTransform.\n\n        Parameters\n        ----------\n        in_column:\n            name of processed column\n        regressor:\n            instance of sklearn :py:class`sklearn.base.RegressorMixin` to predict trend\n        poly_degree:\n            degree of polynomial to fit trend on\n        ')), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Store())], value=Name(id='in_column', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='poly_degree', ctx=Store())], value=Name(id='poly_degree', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_pipeline', ctx=Store())], value=Call(func=Name(id='Pipeline', ctx=Load()), args=[List(elts=[Tuple(elts=[Constant(value='polynomial'), Call(func=Name(id='PolynomialFeatures', ctx=Load()), args=[], keywords=[keyword(arg='degree', value=Attribute(value=Name(id='self', ctx=Load()), attr='poly_degree', ctx=Load())), keyword(arg='include_bias', value=Constant(value=False))])], ctx=Load()), Tuple(elts=[Constant(value='regressor'), Name(id='regressor', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_x_median', ctx=Store())], value=Constant(value=None))], decorator_list=[]), FunctionDef(name='_get_x', args=arguments(posonlyargs=[], args=[arg(arg='df')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='series_len', ctx=Store())], value=Call(func=Name(id='len', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='df', ctx=Load()), attr='index', ctx=Load()), attr='to_series', ctx=Load()), args=[], keywords=[])), If(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Call(func=Name(id='type', ctx=Load()), args=[Attribute(value=Name(id='x', ctx=Load()), attr='dtype', ctx=Load())], keywords=[]), Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load())], keywords=[]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Your timestamp column has wrong format. Need np.datetime64 or datetime.datetime')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Name(id='x', ctx=Load()), attr='apply', ctx=Load()), args=[Lambda(args=arguments(posonlyargs=[], args=[arg(arg='ts')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Attribute(value=Name(id='ts', ctx=Load()), attr='timestamp', ctx=Load()), args=[], keywords=[]))], keywords=[])), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='x', ctx=Load()), attr='to_numpy', ctx=Load()), args=[], keywords=[]), attr='reshape', ctx=Load()), args=[Name(id='series_len', ctx=Load()), Constant(value=1)], keywords=[])), Return(value=Name(id='x', ctx=Load()))], decorator_list=[Name(id='staticmethod', ctx=Load())], returns=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load())), FunctionDef(name='fit', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\n        Fit regression detrend_model with data from df.\n\n        Parameters\n        ----------\n        df:\n            data that regressor should be trained with\n\n        Returns\n        -------\n        _OneSegmentLinearTrendBaseTransform\n            instance with trained regressor\n        ')), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='dropna', ctx=Load()), args=[], keywords=[keyword(arg='subset', value=List(elts=[Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load()))])), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_x', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_x_median', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='median', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[])), AugAssign(target=Name(id='x', ctx=Store()), op=Sub(), value=Attribute(value=Name(id='self', ctx=Load()), attr='_x_median', ctx=Load())), Assign(targets=[Name(id='y', ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Name(id='df', ctx=Load()), slice=Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load()), ctx=Load()), attr='tolist', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_pipeline', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='x', ctx=Load()), Name(id='y', ctx=Load())], keywords=[])), Return(value=Name(id='self', ctx=Load()))], decorator_list=[], returns=Constant(value='_OneSegmentLinearTrendBaseTransform')), FunctionDef(name='transform', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\n        Transform data from df: subtract linear trend found by regressor.\n\n        Parameters\n        ----------\n        df:\n            data to subtract trend from\n\n        Returns\n        -------\n        pd.DataFrame\n            residue after trend subtraction\n        ')), Assign(targets=[Name(id='result', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_x', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])), AugAssign(target=Name(id='x', ctx=Store()), op=Sub(), value=Attribute(value=Name(id='self', ctx=Load()), attr='_x_median', ctx=Load())), Assign(targets=[Name(id='y', ctx=Store())], value=Attribute(value=Subscript(value=Name(id='df', ctx=Load()), slice=Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load()), ctx=Load()), attr='values', ctx=Load())), Assign(targets=[Name(id='trend', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_pipeline', ctx=Load()), attr='predict', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[])), Assign(targets=[Name(id='no_trend_timeseries', ctx=Store())], value=BinOp(left=Name(id='y', ctx=Load()), op=Sub(), right=Name(id='trend', ctx=Load()))), Assign(targets=[Subscript(value=Name(id='result', ctx=Load()), slice=Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load()), ctx=Store())], value=Name(id='no_trend_timeseries', ctx=Load())), Return(value=Name(id='result', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='fit_transform', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\n        Fit regression detrend_model with data from df and subtract the trend from df.\n\n        Parameters\n        ----------\n        df:\n            data to train regressor and transform\n\n        Returns\n        -------\n        pd.DataFrame\n            residue after trend subtraction\n        ')), Return(value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[]), attr='transform', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[]))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='inverse_transform', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\n        Inverse transformation for trend subtraction: add trend to prediction.\n\n        Parameters\n        ----------\n        df:\n            data to transform\n\n        Returns\n        -------\n        pd.DataFrame\n            data with reconstructed trend\n        ')), Assign(targets=[Name(id='result', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_x', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[])), AugAssign(target=Name(id='x', ctx=Store()), op=Sub(), value=Attribute(value=Name(id='self', ctx=Load()), attr='_x_median', ctx=Load())), Assign(targets=[Name(id='y', ctx=Store())], value=Attribute(value=Subscript(value=Name(id='df', ctx=Load()), slice=Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load()), ctx=Load()), attr='values', ctx=Load())), Assign(targets=[Name(id='trend', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_pipeline', ctx=Load()), attr='predict', ctx=Load()), args=[Name(id='x', ctx=Load())], keywords=[])), Assign(targets=[Name(id='add_trend_timeseries', ctx=Store())], value=BinOp(left=Name(id='y', ctx=Load()), op=Add(), right=Name(id='trend', ctx=Load()))), Assign(targets=[Subscript(value=Name(id='result', ctx=Load()), slice=Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load()), ctx=Store())], value=Name(id='add_trend_timeseries', ctx=Load())), If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load()), ops=[Eq()], comparators=[Constant(value='target')]), body=[Assign(targets=[Name(id='quantiles', ctx=Store())], value=Call(func=Name(id='match_target_quantiles', ctx=Load()), args=[Call(func=Name(id='set', ctx=Load()), args=[Attribute(value=Name(id='result', ctx=Load()), attr='columns', ctx=Load())], keywords=[])], keywords=[])), For(target=Name(id='quantile_column_nm', ctx=Store()), iter=Name(id='quantiles', ctx=Load()), body=[AugAssign(target=Subscript(value=Attribute(value=Name(id='result', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='quantile_column_nm', ctx=Load())], ctx=Load()), ctx=Store()), op=Add(), value=Name(id='trend', ctx=Load()))], orelse=[])], orelse=[]), Return(value=Name(id='result', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], decorator_list=[]), ClassDef(name='LinearTrendTransform', bases=[Name(id='PerSegmentWrapper', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='\n    Transform that uses :py:class:`sklearn.linear_model.LinearRegression` to find linear or polynomial trend in data.\n\n    Warning\n    -------\n    This transform can suffer from look-ahead bias. For transforming data at some timestamp\n    it uses information from the whole train part.\n    ')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='in_column', annotation=Name(id='str', ctx=Load())), arg(arg='poly_degree', annotation=Name(id='int', ctx=Load()))], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='regression_params'), defaults=[Constant(value=1)]), body=[Expr(value=Constant(value='Create instance of LinearTrendTransform.\n\n        Parameters\n        ----------\n        in_column:\n            name of processed column\n        poly_degree:\n            degree of polynomial to fit trend on\n        regression_params:\n            params that should be used to init :py:class:`sklearn.linear_model.LinearRegression`\n        ')), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Store())], value=Name(id='in_column', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='poly_degree', ctx=Store())], value=Name(id='poly_degree', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='regression_params', ctx=Store())], value=Name(id='regression_params', ctx=Load())), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='transform', value=Call(func=Name(id='_OneSegmentLinearTrendBaseTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())), keyword(arg='regressor', value=Call(func=Name(id='LinearRegression', ctx=Load()), args=[], keywords=[keyword(value=Attribute(value=Name(id='self', ctx=Load()), attr='regression_params', ctx=Load()))])), keyword(arg='poly_degree', value=Attribute(value=Name(id='self', ctx=Load()), attr='poly_degree', ctx=Load()))]))]))], decorator_list=[])], decorator_list=[]), ClassDef(name='TheilSenTrendTransform', bases=[Name(id='PerSegmentWrapper', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='\n    Transform that uses :py:class:`sklearn.linear_model.TheilSenRegressor` to find linear or polynomial trend in data.\n\n    Warning\n    -------\n    This transform can suffer from look-ahead bias. For transforming data at some timestamp\n    it uses information from the whole train part.\n\n    Notes\n    -----\n    Setting parameter ``n_subsamples`` manually might cause the error. It should be at least the number\n    of features (plus 1 if ``fit_intercept=True``) and the number of samples in the shortest segment as a maximum.\n    ')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='in_column', annotation=Name(id='str', ctx=Load())), arg(arg='poly_degree', annotation=Name(id='int', ctx=Load()))], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='regression_params'), defaults=[Constant(value=1)]), body=[Expr(value=Constant(value='Create instance of TheilSenTrendTransform.\n\n        Parameters\n        ----------\n        in_column:\n            name of processed column\n        poly_degree:\n            degree of polynomial to fit trend on\n        regression_params:\n            params that should be used to init :py:class:`sklearn.linear_model.TheilSenRegressor`\n        ')), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Store())], value=Name(id='in_column', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='poly_degree', ctx=Store())], value=Name(id='poly_degree', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='regression_params', ctx=Store())], value=Name(id='regression_params', ctx=Load())), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='transform', value=Call(func=Name(id='_OneSegmentLinearTrendBaseTransform', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())), keyword(arg='regressor', value=Call(func=Name(id='TheilSenRegressor', ctx=Load()), args=[], keywords=[keyword(value=Attribute(value=Name(id='self', ctx=Load()), attr='regression_params', ctx=Load()))])), keyword(arg='poly_degree', value=Attribute(value=Name(id='self', ctx=Load()), attr='poly_degree', ctx=Load()))]))]))], decorator_list=[])], decorator_list=[])], type_ignores=[])
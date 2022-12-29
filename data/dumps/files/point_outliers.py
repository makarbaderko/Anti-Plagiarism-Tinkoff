Module(body=[ImportFrom(module='typing', names=[alias(name='Callable')], level=0), ImportFrom(module='typing', names=[alias(name='Dict')], level=0), ImportFrom(module='typing', names=[alias(name='List')], level=0), ImportFrom(module='typing', names=[alias(name='Type')], level=0), ImportFrom(module='typing', names=[alias(name='Union')], level=0), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='etna', names=[alias(name='SETTINGS')], level=0), ImportFrom(module='etna.analysis', names=[alias(name='absolute_difference_distance')], level=0), ImportFrom(module='etna.analysis', names=[alias(name='get_anomalies_density')], level=0), ImportFrom(module='etna.analysis', names=[alias(name='get_anomalies_median')], level=0), ImportFrom(module='etna.analysis', names=[alias(name='get_anomalies_prediction_interval')], level=0), ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0), ImportFrom(module='etna.models', names=[alias(name='SARIMAXModel')], level=0), ImportFrom(module='etna.transforms.outliers.base', names=[alias(name='OutliersTransform')], level=0), If(test=Attribute(value=Name(id='SETTINGS', ctx=Load()), attr='prophet_required', ctx=Load()), body=[ImportFrom(module='etna.models', names=[alias(name='ProphetModel')], level=0)], orelse=[]), ClassDef(name='MedianOutliersTransform', bases=[Name(id='OutliersTransform', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Transform that uses :py:func:`~etna.analysis.outliers.median_outliers.get_anomalies_median` to find anomalies in data.\n\n    Warning\n    -------\n    This transform can suffer from look-ahead bias. For transforming data at some timestamp\n    it uses information from the whole train part.\n    ')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='in_column', annotation=Name(id='str', ctx=Load())), arg(arg='window_size', annotation=Name(id='int', ctx=Load())), arg(arg='alpha', annotation=Name(id='float', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=10), Constant(value=3)]), body=[Expr(value=Constant(value='Create instance of MedianOutliersTransform.\n\n        Parameters\n        ----------\n        in_column:\n            name of processed column\n        window_size:\n            number of points in the window\n        alpha:\n            coefficient for determining the threshold\n        ')), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='window_size', ctx=Store())], value=Name(id='window_size', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='alpha', ctx=Store())], value=Name(id='alpha', ctx=Load())), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Name(id='in_column', ctx=Load()))]))], decorator_list=[]), FunctionDef(name='detect_outliers', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Call :py:func:`~etna.analysis.outliers.median_outliers.get_anomalies_median` function with self parameters.\n\n        Parameters\n        ----------\n        ts:\n            dataset to process\n\n        Returns\n        -------\n        :\n            dict of outliers in format {segment: [outliers_timestamps]}\n        ')), Return(value=Call(func=Name(id='get_anomalies_median', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='in_column', value=Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())), keyword(arg='window_size', value=Attribute(value=Name(id='self', ctx=Load()), attr='window_size', ctx=Load())), keyword(arg='alpha', value=Attribute(value=Name(id='self', ctx=Load()), attr='alpha', ctx=Load()))]))], decorator_list=[], returns=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Subscript(value=Name(id='List', ctx=Load()), slice=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()))], decorator_list=[]), ClassDef(name='DensityOutliersTransform', bases=[Name(id='OutliersTransform', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Transform that uses :py:func:`~etna.analysis.outliers.density_outliers.get_anomalies_density` to find anomalies in data.\n\n    Warning\n    -------\n    This transform can suffer from look-ahead bias. For transforming data at some timestamp\n    it uses information from the whole train part.\n    ')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='in_column', annotation=Name(id='str', ctx=Load())), arg(arg='window_size', annotation=Name(id='int', ctx=Load())), arg(arg='distance_coef', annotation=Name(id='float', ctx=Load())), arg(arg='n_neighbors', annotation=Name(id='int', ctx=Load())), arg(arg='distance_func', annotation=Subscript(value=Name(id='Callable', ctx=Load()), slice=Tuple(elts=[List(elts=[Name(id='float', ctx=Load()), Name(id='float', ctx=Load())], ctx=Load()), Name(id='float', ctx=Load())], ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=15), Constant(value=3), Constant(value=3), Name(id='absolute_difference_distance', ctx=Load())]), body=[Expr(value=Constant(value='Create instance of DensityOutliersTransform.\n\n        Parameters\n        ----------\n        in_column:\n            name of processed column\n        window_size:\n            size of windows to build\n        distance_coef:\n            factor for standard deviation that forms distance threshold to determine points are close to each other\n        n_neighbors:\n            min number of close neighbors of point not to be outlier\n        distance_func:\n            distance function\n        ')), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='window_size', ctx=Store())], value=Name(id='window_size', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='distance_coef', ctx=Store())], value=Name(id='distance_coef', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='n_neighbors', ctx=Store())], value=Name(id='n_neighbors', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='distance_func', ctx=Store())], value=Name(id='distance_func', ctx=Load())), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Name(id='in_column', ctx=Load()))]))], decorator_list=[]), FunctionDef(name='detect_outliers', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Call :py:func:`~etna.analysis.outliers.density_outliers.get_anomalies_density` function with self parameters.\n\n        Parameters\n        ----------\n        ts:\n            dataset to process\n\n        Returns\n        -------\n        :\n            dict of outliers in format {segment: [outliers_timestamps]}\n        ')), Return(value=Call(func=Name(id='get_anomalies_density', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='in_column', value=Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())), keyword(arg='window_size', value=Attribute(value=Name(id='self', ctx=Load()), attr='window_size', ctx=Load())), keyword(arg='distance_coef', value=Attribute(value=Name(id='self', ctx=Load()), attr='distance_coef', ctx=Load())), keyword(arg='n_neighbors', value=Attribute(value=Name(id='self', ctx=Load()), attr='n_neighbors', ctx=Load())), keyword(arg='distance_func', value=Attribute(value=Name(id='self', ctx=Load()), attr='distance_func', ctx=Load()))]))], decorator_list=[], returns=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Subscript(value=Name(id='List', ctx=Load()), slice=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()))], decorator_list=[]), ClassDef(name='PredictionIntervalOutliersTransform', bases=[Name(id='OutliersTransform', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Transform that uses :py:func:`~etna.analysis.outliers.prediction_interval_outliers.get_anomalies_prediction_interval` to find anomalies in data.')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='in_column', annotation=Name(id='str', ctx=Load())), arg(arg='model', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Subscript(value=Name(id='Type', ctx=Load()), slice=Constant(value='ProphetModel'), ctx=Load()), Subscript(value=Name(id='Type', ctx=Load()), slice=Constant(value='SARIMAXModel'), ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='interval_width', annotation=Name(id='float', ctx=Load()))], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='model_kwargs'), defaults=[Constant(value=0.95)]), body=[Expr(value=Constant(value='Create instance of PredictionIntervalOutliersTransform.\n\n        Parameters\n        ----------\n        in_column:\n            name of processed column\n        model:\n            model for prediction interval estimation\n        interval_width:\n            width of the prediction interval\n\n        Notes\n        -----\n        For not "target" column only column data will be used for learning.\n        ')), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Store())], value=Name(id='model', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='interval_width', ctx=Store())], value=Name(id='interval_width', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='model_kwargs', ctx=Store())], value=Name(id='model_kwargs', ctx=Load())), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Name(id='in_column', ctx=Load()))]))], decorator_list=[]), FunctionDef(name='detect_outliers', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Call :py:func:`~etna.analysis.outliers.prediction_interval_outliers.get_anomalies_prediction_interval` function with self parameters.\n\n        Parameters\n        ----------\n        ts:\n            dataset to process\n\n        Returns\n        -------\n        :\n            dict of outliers in format {segment: [outliers_timestamps]}\n        ')), Return(value=Call(func=Name(id='get_anomalies_prediction_interval', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='model', value=Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load())), keyword(arg='interval_width', value=Attribute(value=Name(id='self', ctx=Load()), attr='interval_width', ctx=Load())), keyword(arg='in_column', value=Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())), keyword(value=Attribute(value=Name(id='self', ctx=Load()), attr='model_kwargs', ctx=Load()))]))], decorator_list=[], returns=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Subscript(value=Name(id='List', ctx=Load()), slice=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()))], decorator_list=[]), Assign(targets=[Name(id='__all__', ctx=Store())], value=List(elts=[Constant(value='MedianOutliersTransform'), Constant(value='DensityOutliersTransform'), Constant(value='PredictionIntervalOutliersTransform')], ctx=Load()))], type_ignores=[])
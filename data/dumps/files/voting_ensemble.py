Module(body=[ImportFrom(module='copy', names=[alias(name='deepcopy')], level=0), ImportFrom(module='typing', names=[alias(name='Any')], level=0), ImportFrom(module='typing', names=[alias(name='Dict')], level=0), ImportFrom(module='typing', names=[alias(name='List')], level=0), ImportFrom(module='typing', names=[alias(name='Optional')], level=0), ImportFrom(module='typing', names=[alias(name='Sequence')], level=0), ImportFrom(module='typing', names=[alias(name='Union')], level=0), ImportFrom(module='typing', names=[alias(name='cast')], level=0), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='joblib', names=[alias(name='Parallel')], level=0), ImportFrom(module='joblib', names=[alias(name='delayed')], level=0), ImportFrom(module='sklearn.ensemble', names=[alias(name='RandomForestRegressor')], level=0), ImportFrom(module='typing_extensions', names=[alias(name='Literal')], level=0), ImportFrom(module='etna.analysis.feature_relevance.relevance_table', names=[alias(name='TreeBasedRegressor')], level=0), ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0), ImportFrom(module='etna.ensembles', names=[alias(name='EnsembleMixin')], level=0), ImportFrom(module='etna.loggers', names=[alias(name='tslogger')], level=0), ImportFrom(module='etna.metrics', names=[alias(name='MAE')], level=0), ImportFrom(module='etna.pipeline.base', names=[alias(name='BasePipeline')], level=0), ClassDef(name='VotingEnsemble', bases=[Name(id='BasePipeline', ctx=Load()), Name(id='EnsembleMixin', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='VotingEnsemble is a pipeline that forecast future values with weighted averaging of it\'s pipelines forecasts.\n\n    Examples\n    --------\n    >>> from etna.datasets import generate_ar_df\n    >>> from etna.datasets import TSDataset\n    >>> from etna.ensembles import VotingEnsemble\n    >>> from etna.models import NaiveModel\n    >>> from etna.models import ProphetModel\n    >>> from etna.pipeline import Pipeline\n    >>> df = generate_ar_df(periods=30, start_time="2021-06-01", ar_coef=[1.2], n_segments=3)\n    >>> df_ts_format = TSDataset.to_dataset(df)\n    >>> ts = TSDataset(df_ts_format, "D")\n    >>> prophet_pipeline = Pipeline(model=ProphetModel(), transforms=[], horizon=7)\n    >>> naive_pipeline = Pipeline(model=NaiveModel(lag=10), transforms=[], horizon=7)\n    >>> ensemble = VotingEnsemble(\n    ...     pipelines=[prophet_pipeline, naive_pipeline],\n    ...     weights=[0.7, 0.3]\n    ... )\n    >>> _ = ensemble.fit(ts=ts)\n    >>> forecast = ensemble.forecast()\n    >>> forecast\n    segment         segment_0        segment_1       segment_2\n    feature\t       target           target\t        target\n    timestamp\n    2021-07-01\t        -8.84\t       -186.67\t        130.99\n    2021-07-02\t        -8.96\t       -198.16\t        138.81\n    2021-07-03\t        -9.57\t       -212.48\t        148.48\n    2021-07-04\t       -10.48\t       -229.16\t        160.13\n    2021-07-05\t       -11.20          -248.93\t        174.39\n    2021-07-06\t       -12.47\t       -281.90\t        197.82\n    2021-07-07\t       -13.51\t       -307.02\t        215.73\n    ')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='pipelines', annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='BasePipeline', ctx=Load()), ctx=Load())), arg(arg='weights', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='float', ctx=Load()), ctx=Load()), Subscript(value=Name(id='Literal', ctx=Load()), slice=Constant(value='auto'), ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load())), arg(arg='regressor', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='TreeBasedRegressor', ctx=Load()), ctx=Load())), arg(arg='n_folds', annotation=Name(id='int', ctx=Load())), arg(arg='n_jobs', annotation=Name(id='int', ctx=Load())), arg(arg='joblib_params', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='Any', ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None), Constant(value=None), Constant(value=3), Constant(value=1), Constant(value=None)]), body=[Expr(value=Constant(value='Init VotingEnsemble.\n\n        Parameters\n        ----------\n        pipelines:\n            List of pipelines that should be used in ensemble\n        weights:\n            List of pipelines\' weights.\n\n            * If None, use uniform weights\n\n            * If List[float], use this weights for the base estimators, weights will be normalized automatically\n\n            * If "auto", use importances of the base estimators forecasts as weights of base estimators\n\n        regressor:\n            Regression model with fit/predict interface which will be used to evaluate weights of the base estimators.\n            It should have ``feature_importances_`` property (e.g. all tree-based regressors in sklearn)\n        n_folds:\n            Number of folds to use in the backtest.\n            Backtest is used to obtain the forecasts from the base estimators;\n            forecasts will be used to evaluate the estimator\'s weights.\n        n_jobs:\n            Number of jobs to run in parallel\n        joblib_params:\n            Additional parameters for :py:class:`joblib.Parallel`\n\n        Raises\n        ------\n        ValueError:\n            If the number of the pipelines is less than 2 or pipelines have different horizons.\n        ')), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_validate_pipeline_number', ctx=Load()), args=[], keywords=[keyword(arg='pipelines', value=Name(id='pipelines', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_validate_weights', ctx=Load()), args=[], keywords=[keyword(arg='weights', value=Name(id='weights', ctx=Load())), keyword(arg='pipelines_number', value=Call(func=Name(id='len', ctx=Load()), args=[Name(id='pipelines', ctx=Load())], keywords=[]))])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_validate_backtest_n_folds', ctx=Load()), args=[Name(id='n_folds', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='weights', ctx=Store())], value=Name(id='weights', ctx=Load())), AnnAssign(target=Attribute(value=Name(id='self', ctx=Load()), attr='processed_weights', ctx=Store()), annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='float', ctx=Load()), ctx=Load()), ctx=Load()), value=Constant(value=None), simple=0), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='regressor', ctx=Store())], value=IfExp(test=Compare(left=Name(id='regressor', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=Call(func=Name(id='RandomForestRegressor', ctx=Load()), args=[], keywords=[keyword(arg='n_estimators', value=Constant(value=5))]), orelse=Name(id='regressor', ctx=Load()))), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='n_folds', ctx=Store())], value=Name(id='n_folds', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='pipelines', ctx=Store())], value=Name(id='pipelines', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='n_jobs', ctx=Store())], value=Name(id='n_jobs', ctx=Load())), If(test=Compare(left=Name(id='joblib_params', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='joblib_params', ctx=Store())], value=Call(func=Name(id='dict', ctx=Load()), args=[], keywords=[keyword(arg='verbose', value=Constant(value=11)), keyword(arg='backend', value=Constant(value='multiprocessing')), keyword(arg='mmap_mode', value=Constant(value='c'))]))], orelse=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='joblib_params', ctx=Store())], value=Name(id='joblib_params', ctx=Load()))]), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='horizon', value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_horizon', ctx=Load()), args=[], keywords=[keyword(arg='pipelines', value=Name(id='pipelines', ctx=Load()))]))]))], decorator_list=[]), FunctionDef(name='_validate_weights', args=arguments(posonlyargs=[], args=[arg(arg='weights', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='float', ctx=Load()), ctx=Load()), Subscript(value=Name(id='Literal', ctx=Load()), slice=Constant(value='auto'), ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load())), arg(arg='pipelines_number', annotation=Name(id='int', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Validate the format of weights parameter.')), If(test=BoolOp(op=Or(), values=[Compare(left=Name(id='weights', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), Compare(left=Name(id='weights', ctx=Load()), ops=[Eq()], comparators=[Constant(value='auto')])]), body=[Pass()], orelse=[If(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='weights', ctx=Load()), Name(id='list', ctx=Load())], keywords=[]), body=[If(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='weights', ctx=Load())], keywords=[]), ops=[NotEq()], comparators=[Name(id='pipelines_number', ctx=Load())]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Weights size should be equal to pipelines number.')], keywords=[]))], orelse=[])], orelse=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Invalid format of weights is passed!')], keywords=[]))])])], decorator_list=[Name(id='staticmethod', ctx=Load())]), FunctionDef(name='_backtest_pipeline', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='pipeline', annotation=Name(id='BasePipeline', ctx=Load())), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Get forecasts from backtest for given pipeline.')), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='tslogger', ctx=Load()), attr='disable', ctx=Load()), args=[], keywords=[]))], body=[Assign(targets=[Tuple(elts=[Name(id='_', ctx=Store()), Name(id='forecasts', ctx=Store()), Name(id='_', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='pipeline', ctx=Load()), attr='backtest', ctx=Load()), args=[Name(id='ts', ctx=Load())], keywords=[keyword(arg='metrics', value=List(elts=[Call(func=Name(id='MAE', ctx=Load()), args=[], keywords=[])], ctx=Load())), keyword(arg='n_folds', value=Attribute(value=Name(id='self', ctx=Load()), attr='n_folds', ctx=Load()))]))]), Assign(targets=[Name(id='forecasts', ctx=Store())], value=Call(func=Name(id='TSDataset', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='forecasts', ctx=Load())), keyword(arg='freq', value=Attribute(value=Name(id='ts', ctx=Load()), attr='freq', ctx=Load()))])), Return(value=Name(id='forecasts', ctx=Load()))], decorator_list=[], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='_process_weights', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Get the weights of base estimators depending on the weights mode.')), If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='weights', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Assign(targets=[Name(id='weights', ctx=Store())], value=ListComp(elt=Constant(value=1.0), generators=[comprehension(target=Name(id='_', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Call(func=Name(id='len', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='pipelines', ctx=Load())], keywords=[])], keywords=[]), ifs=[], is_async=0)]))], orelse=[If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='weights', ctx=Load()), ops=[Eq()], comparators=[Constant(value='auto')]), body=[If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Something went wrong, ts is None!')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='forecasts', ctx=Store())], value=Call(func=Call(func=Name(id='Parallel', ctx=Load()), args=[], keywords=[keyword(arg='n_jobs', value=Attribute(value=Name(id='self', ctx=Load()), attr='n_jobs', ctx=Load())), keyword(value=Attribute(value=Name(id='self', ctx=Load()), attr='joblib_params', ctx=Load()))]), args=[GeneratorExp(elt=Call(func=Call(func=Name(id='delayed', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_backtest_pipeline', ctx=Load())], keywords=[]), args=[], keywords=[keyword(arg='pipeline', value=Name(id='pipeline', ctx=Load())), keyword(arg='ts', value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load())], keywords=[]))]), generators=[comprehension(target=Name(id='pipeline', ctx=Store()), iter=Attribute(value=Name(id='self', ctx=Load()), attr='pipelines', ctx=Load()), ifs=[], is_async=0)])], keywords=[])), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[ListComp(elt=Call(func=Attribute(value=Subscript(value=Name(id='forecast', ctx=Load()), slice=Tuple(elts=[Slice(), Slice(), Constant(value='target')], ctx=Load()), ctx=Load()), attr='rename', ctx=Load()), args=[Dict(keys=[Constant(value='target')], values=[JoinedStr(values=[Constant(value='target_'), FormattedValue(value=Name(id='i', ctx=Load()), conversion=-1)])])], keywords=[keyword(arg='axis', value=Constant(value=1))]), generators=[comprehension(target=Tuple(elts=[Name(id='i', ctx=Store()), Name(id='forecast', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='enumerate', ctx=Load()), args=[Name(id='forecasts', ctx=Load())], keywords=[]), ifs=[], is_async=0)])], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Name(id='x', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[ListComp(elt=Subscript(value=Attribute(value=Name(id='x', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='segment', ctx=Load())], ctx=Load()), ctx=Load()), generators=[comprehension(target=Name(id='segment', ctx=Store()), iter=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), attr='segments', ctx=Load()), ifs=[], is_async=0)])], keywords=[keyword(arg='axis', value=Constant(value=0))])), Assign(targets=[Name(id='y', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[ListComp(elt=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), slice=Tuple(elts=[Slice(lower=Call(func=Attribute(value=Attribute(value=Subscript(value=Name(id='forecasts', ctx=Load()), slice=Constant(value=0), ctx=Load()), attr='index', ctx=Load()), attr='min', ctx=Load()), args=[], keywords=[]), upper=Call(func=Attribute(value=Attribute(value=Subscript(value=Name(id='forecasts', ctx=Load()), slice=Constant(value=0), ctx=Load()), attr='index', ctx=Load()), attr='max', ctx=Load()), args=[], keywords=[])), Name(id='segment', ctx=Load()), Constant(value='target')], ctx=Load()), ctx=Load()), generators=[comprehension(target=Name(id='segment', ctx=Store()), iter=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), attr='segments', ctx=Load()), ifs=[], is_async=0)])], keywords=[keyword(arg='axis', value=Constant(value=0))])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='regressor', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='x', ctx=Load()), Name(id='y', ctx=Load())], keywords=[])), Assign(targets=[Name(id='weights', ctx=Store())], value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='regressor', ctx=Load()), attr='feature_importances_', ctx=Load()))], orelse=[Assign(targets=[Name(id='weights', ctx=Store())], value=Attribute(value=Name(id='self', ctx=Load()), attr='weights', ctx=Load()))])]), Assign(targets=[Name(id='common_weight', ctx=Store())], value=Call(func=Name(id='sum', ctx=Load()), args=[Name(id='weights', ctx=Load())], keywords=[])), Assign(targets=[Name(id='weights', ctx=Store())], value=ListComp(elt=BinOp(left=Name(id='w', ctx=Load()), op=Div(), right=Name(id='common_weight', ctx=Load())), generators=[comprehension(target=Name(id='w', ctx=Store()), iter=Name(id='weights', ctx=Load()), ifs=[], is_async=0)])), Return(value=Name(id='weights', ctx=Load()))], decorator_list=[], returns=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='float', ctx=Load()), ctx=Load())), FunctionDef(name='fit', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Fit pipelines in ensemble.\n\n        Parameters\n        ----------\n        ts:\n            TSDataset to fit ensemble\n\n        Returns\n        -------\n        self:\n            Fitted ensemble\n        ')), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Store())], value=Name(id='ts', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='pipelines', ctx=Store())], value=Call(func=Call(func=Name(id='Parallel', ctx=Load()), args=[], keywords=[keyword(arg='n_jobs', value=Attribute(value=Name(id='self', ctx=Load()), attr='n_jobs', ctx=Load())), keyword(value=Attribute(value=Name(id='self', ctx=Load()), attr='joblib_params', ctx=Load()))]), args=[GeneratorExp(elt=Call(func=Call(func=Name(id='delayed', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_fit_pipeline', ctx=Load())], keywords=[]), args=[], keywords=[keyword(arg='pipeline', value=Name(id='pipeline', ctx=Load())), keyword(arg='ts', value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Name(id='ts', ctx=Load())], keywords=[]))]), generators=[comprehension(target=Name(id='pipeline', ctx=Store()), iter=Attribute(value=Name(id='self', ctx=Load()), attr='pipelines', ctx=Load()), ifs=[], is_async=0)])], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='processed_weights', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_process_weights', ctx=Load()), args=[], keywords=[])), Return(value=Name(id='self', ctx=Load()))], decorator_list=[], returns=Constant(value='VotingEnsemble')), FunctionDef(name='_vote', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='forecasts', annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='TSDataset', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Get average forecast.')), If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='processed_weights', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Ensemble is not fitted! Fit the ensemble before calling the forecast!')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='forecast_df', ctx=Store())], value=Call(func=Name(id='sum', ctx=Load()), args=[ListComp(elt=BinOp(left=Subscript(value=Name(id='forecast', ctx=Load()), slice=Tuple(elts=[Slice(), Slice(), Constant(value='target')], ctx=Load()), ctx=Load()), op=Mult(), right=Name(id='weight', ctx=Load())), generators=[comprehension(target=Tuple(elts=[Name(id='forecast', ctx=Store()), Name(id='weight', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='zip', ctx=Load()), args=[Name(id='forecasts', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='processed_weights', ctx=Load())], keywords=[]), ifs=[], is_async=0)])], keywords=[])), Assign(targets=[Name(id='forecast_dataset', ctx=Store())], value=Call(func=Name(id='TSDataset', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='forecast_df', ctx=Load())), keyword(arg='freq', value=Attribute(value=Subscript(value=Name(id='forecasts', ctx=Load()), slice=Constant(value=0), ctx=Load()), attr='freq', ctx=Load()))])), Return(value=Name(id='forecast_dataset', ctx=Load()))], decorator_list=[], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='_forecast', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value="Make predictions.\n\n        Compute weighted average of pipelines' forecasts\n        ")), If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Something went wrong, ts is None!')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='forecasts', ctx=Store())], value=Call(func=Call(func=Name(id='Parallel', ctx=Load()), args=[], keywords=[keyword(arg='n_jobs', value=Attribute(value=Name(id='self', ctx=Load()), attr='n_jobs', ctx=Load())), keyword(arg='backend', value=Constant(value='multiprocessing')), keyword(arg='verbose', value=Constant(value=11))]), args=[GeneratorExp(elt=Call(func=Call(func=Name(id='delayed', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_forecast_pipeline', ctx=Load())], keywords=[]), args=[], keywords=[keyword(arg='pipeline', value=Name(id='pipeline', ctx=Load()))]), generators=[comprehension(target=Name(id='pipeline', ctx=Store()), iter=Attribute(value=Name(id='self', ctx=Load()), attr='pipelines', ctx=Load()), ifs=[], is_async=0)])], keywords=[])), Assign(targets=[Name(id='forecast', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_vote', ctx=Load()), args=[], keywords=[keyword(arg='forecasts', value=Name(id='forecasts', ctx=Load()))])), Return(value=Name(id='forecast', ctx=Load()))], decorator_list=[], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='_predict', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load())), arg(arg='start_timestamp', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load())), arg(arg='end_timestamp', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load())), arg(arg='prediction_interval', annotation=Name(id='bool', ctx=Load())), arg(arg='quantiles', annotation=Subscript(value=Name(id='Sequence', ctx=Load()), slice=Name(id='float', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Name(id='prediction_interval', ctx=Load()), body=[Raise(exc=Call(func=Name(id='NotImplementedError', ctx=Load()), args=[JoinedStr(values=[Constant(value='Ensemble '), FormattedValue(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='__class__', ctx=Load()), attr='__name__', ctx=Load()), conversion=-1), Constant(value=" doesn't support prediction intervals!")])], keywords=[]))], orelse=[]), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Store())], value=Call(func=Name(id='cast', ctx=Load()), args=[Name(id='TSDataset', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load())], keywords=[])), Assign(targets=[Name(id='predictions', ctx=Store())], value=Call(func=Call(func=Name(id='Parallel', ctx=Load()), args=[], keywords=[keyword(arg='n_jobs', value=Attribute(value=Name(id='self', ctx=Load()), attr='n_jobs', ctx=Load())), keyword(arg='backend', value=Constant(value='multiprocessing')), keyword(arg='verbose', value=Constant(value=11))]), args=[GeneratorExp(elt=Call(func=Call(func=Name(id='delayed', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_predict_pipeline', ctx=Load())], keywords=[]), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='pipeline', value=Name(id='pipeline', ctx=Load())), keyword(arg='start_timestamp', value=Name(id='start_timestamp', ctx=Load())), keyword(arg='end_timestamp', value=Name(id='end_timestamp', ctx=Load()))]), generators=[comprehension(target=Name(id='pipeline', ctx=Store()), iter=Attribute(value=Name(id='self', ctx=Load()), attr='pipelines', ctx=Load()), ifs=[], is_async=0)])], keywords=[])), Assign(targets=[Name(id='predictions', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_vote', ctx=Load()), args=[], keywords=[keyword(arg='forecasts', value=Name(id='predictions', ctx=Load()))])), Return(value=Name(id='predictions', ctx=Load()))], decorator_list=[], returns=Name(id='TSDataset', ctx=Load()))], decorator_list=[])], type_ignores=[])
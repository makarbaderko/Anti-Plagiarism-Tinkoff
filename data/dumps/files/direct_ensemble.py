Module(body=[ImportFrom(module='copy', names=[alias(name='deepcopy')], level=0), ImportFrom(module='typing', names=[alias(name='Any')], level=0), ImportFrom(module='typing', names=[alias(name='Dict')], level=0), ImportFrom(module='typing', names=[alias(name='List')], level=0), ImportFrom(module='typing', names=[alias(name='Optional')], level=0), ImportFrom(module='typing', names=[alias(name='Sequence')], level=0), Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='joblib', names=[alias(name='Parallel')], level=0), ImportFrom(module='joblib', names=[alias(name='delayed')], level=0), ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0), ImportFrom(module='etna.ensembles', names=[alias(name='EnsembleMixin')], level=0), ImportFrom(module='etna.pipeline.base', names=[alias(name='BasePipeline')], level=0), ClassDef(name='DirectEnsemble', bases=[Name(id='BasePipeline', ctx=Load()), Name(id='EnsembleMixin', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='DirectEnsemble is a pipeline that forecasts future values merging the forecasts of base pipelines.\n\n    Ensemble expects several pipelines during init. These pipelines are expected to have different forecasting horizons.\n    For each point in the future, forecast of the ensemble is forecast of base pipeline with the shortest horizon,\n    which covers this point.\n\n    Examples\n    --------\n    >>> from etna.datasets import generate_ar_df\n    >>> from etna.datasets import TSDataset\n    >>> from etna.ensembles import DirectEnsemble\n    >>> from etna.models import NaiveModel\n    >>> from etna.models import ProphetModel\n    >>> from etna.pipeline import Pipeline\n    >>> df = generate_ar_df(periods=30, start_time="2021-06-01", ar_coef=[1.2], n_segments=3)\n    >>> df_ts_format = TSDataset.to_dataset(df)\n    >>> ts = TSDataset(df_ts_format, "D")\n    >>> prophet_pipeline = Pipeline(model=ProphetModel(), transforms=[], horizon=3)\n    >>> naive_pipeline = Pipeline(model=NaiveModel(lag=10), transforms=[], horizon=5)\n    >>> ensemble = DirectEnsemble(pipelines=[prophet_pipeline, naive_pipeline])\n    >>> _ = ensemble.fit(ts=ts)\n    >>> forecast = ensemble.forecast()\n    >>> forecast\n    segment    segment_0 segment_1 segment_2\n    feature       target    target    target\n    timestamp\n    2021-07-01    -10.37   -232.60    163.16\n    2021-07-02    -10.59   -242.05    169.62\n    2021-07-03    -11.41   -253.82    177.62\n    2021-07-04     -5.85   -139.57     96.99\n    2021-07-05     -6.11   -167.69    116.59\n    ')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='pipelines', annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='BasePipeline', ctx=Load()), ctx=Load())), arg(arg='n_jobs', annotation=Name(id='int', ctx=Load())), arg(arg='joblib_params', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='Any', ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=1), Constant(value=None)]), body=[Expr(value=Constant(value='Init DirectEnsemble.\n\n        Parameters\n        ----------\n        pipelines:\n            List of pipelines that should be used in ensemble\n        n_jobs:\n            Number of jobs to run in parallel\n        joblib_params:\n            Additional parameters for :py:class:`joblib.Parallel`\n\n        Raises\n        ------\n        ValueError:\n            If two or more pipelines have the same horizons.\n        ')), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_validate_pipeline_number', ctx=Load()), args=[], keywords=[keyword(arg='pipelines', value=Name(id='pipelines', ctx=Load()))])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='pipelines', ctx=Store())], value=Name(id='pipelines', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='n_jobs', ctx=Store())], value=Name(id='n_jobs', ctx=Load())), If(test=Compare(left=Name(id='joblib_params', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='joblib_params', ctx=Store())], value=Call(func=Name(id='dict', ctx=Load()), args=[], keywords=[keyword(arg='verbose', value=Constant(value=11)), keyword(arg='backend', value=Constant(value='multiprocessing')), keyword(arg='mmap_mode', value=Constant(value='c'))]))], orelse=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='joblib_params', ctx=Store())], value=Name(id='joblib_params', ctx=Load()))]), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='horizon', value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_horizon', ctx=Load()), args=[], keywords=[keyword(arg='pipelines', value=Name(id='pipelines', ctx=Load()))]))]))], decorator_list=[]), FunctionDef(name='_get_horizon', args=arguments(posonlyargs=[], args=[arg(arg='pipelines', annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='BasePipeline', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value="Get ensemble's horizon.")), Assign(targets=[Name(id='horizons', ctx=Store())], value=SetComp(elt=Attribute(value=Name(id='pipeline', ctx=Load()), attr='horizon', ctx=Load()), generators=[comprehension(target=Name(id='pipeline', ctx=Store()), iter=Name(id='pipelines', ctx=Load()), ifs=[], is_async=0)])), If(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='horizons', ctx=Load())], keywords=[]), ops=[NotEq()], comparators=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='pipelines', ctx=Load())], keywords=[])]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='All the pipelines should have pairwise different horizons.')], keywords=[]))], orelse=[]), Return(value=Call(func=Name(id='max', ctx=Load()), args=[Name(id='horizons', ctx=Load())], keywords=[]))], decorator_list=[Name(id='staticmethod', ctx=Load())], returns=Name(id='int', ctx=Load())), FunctionDef(name='fit', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Fit pipelines in ensemble.\n\n        Parameters\n        ----------\n        ts:\n            TSDataset to fit ensemble\n\n        Returns\n        -------\n        self:\n            Fitted ensemble\n        ')), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Store())], value=Name(id='ts', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='pipelines', ctx=Store())], value=Call(func=Call(func=Name(id='Parallel', ctx=Load()), args=[], keywords=[keyword(arg='n_jobs', value=Attribute(value=Name(id='self', ctx=Load()), attr='n_jobs', ctx=Load())), keyword(value=Attribute(value=Name(id='self', ctx=Load()), attr='joblib_params', ctx=Load()))]), args=[GeneratorExp(elt=Call(func=Call(func=Name(id='delayed', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_fit_pipeline', ctx=Load())], keywords=[]), args=[], keywords=[keyword(arg='pipeline', value=Name(id='pipeline', ctx=Load())), keyword(arg='ts', value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Name(id='ts', ctx=Load())], keywords=[]))]), generators=[comprehension(target=Name(id='pipeline', ctx=Store()), iter=Attribute(value=Name(id='self', ctx=Load()), attr='pipelines', ctx=Load()), ifs=[], is_async=0)])], keywords=[])), Return(value=Name(id='self', ctx=Load()))], decorator_list=[], returns=Constant(value='DirectEnsemble')), FunctionDef(name='_merge', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='forecasts', annotation=Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='TSDataset', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Merge the forecasts of base pipelines according to the direct strategy.')), Assign(targets=[Name(id='segments', ctx=Store())], value=Call(func=Name(id='sorted', ctx=Load()), args=[Attribute(value=Subscript(value=Name(id='forecasts', ctx=Load()), slice=Constant(value=0), ctx=Load()), attr='segments', ctx=Load())], keywords=[])), Assign(targets=[Name(id='horizons', ctx=Store())], value=ListComp(elt=Attribute(value=Name(id='pipeline', ctx=Load()), attr='horizon', ctx=Load()), generators=[comprehension(target=Name(id='pipeline', ctx=Store()), iter=Attribute(value=Name(id='self', ctx=Load()), attr='pipelines', ctx=Load()), ifs=[], is_async=0)])), Assign(targets=[Name(id='pipelines_order', ctx=Store())], value=Subscript(value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='argsort', ctx=Load()), args=[Name(id='horizons', ctx=Load())], keywords=[]), slice=Slice(step=UnaryOp(op=USub(), operand=Constant(value=1))), ctx=Load())), Assign(targets=[Name(id='forecast_df', ctx=Store())], value=Subscript(value=Subscript(value=Name(id='forecasts', ctx=Load()), slice=Subscript(value=Name(id='pipelines_order', ctx=Load()), slice=Constant(value=0), ctx=Load()), ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='segments', ctx=Load()), Constant(value='target')], ctx=Load()), ctx=Load())), For(target=Name(id='idx', ctx=Store()), iter=Name(id='pipelines_order', ctx=Load()), body=[Assign(targets=[Tuple(elts=[Name(id='horizon', ctx=Store()), Name(id='forecast', ctx=Store())], ctx=Store())], value=Tuple(elts=[Subscript(value=Name(id='horizons', ctx=Load()), slice=Name(id='idx', ctx=Load()), ctx=Load()), Subscript(value=Subscript(value=Name(id='forecasts', ctx=Load()), slice=Name(id='idx', ctx=Load()), ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='segments', ctx=Load()), Constant(value='target')], ctx=Load()), ctx=Load())], ctx=Load())), Assign(targets=[Subscript(value=Attribute(value=Name(id='forecast_df', ctx=Load()), attr='iloc', ctx=Load()), slice=Slice(upper=Name(id='horizon', ctx=Load())), ctx=Store())], value=Name(id='forecast', ctx=Load()))], orelse=[]), Assign(targets=[Name(id='forecast_dataset', ctx=Store())], value=Call(func=Name(id='TSDataset', ctx=Load()), args=[], keywords=[keyword(arg='df', value=Name(id='forecast_df', ctx=Load())), keyword(arg='freq', value=Attribute(value=Subscript(value=Name(id='forecasts', ctx=Load()), slice=Constant(value=0), ctx=Load()), attr='freq', ctx=Load()))])), Return(value=Name(id='forecast_dataset', ctx=Load()))], decorator_list=[], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='_forecast', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Make predictions.\n\n        In each point in the future, forecast of the ensemble is forecast of base pipeline with the shortest horizon,\n        which covers this point.\n        ')), If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='ts', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Something went wrong, ts is None!')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='forecasts', ctx=Store())], value=Call(func=Call(func=Name(id='Parallel', ctx=Load()), args=[], keywords=[keyword(arg='n_jobs', value=Attribute(value=Name(id='self', ctx=Load()), attr='n_jobs', ctx=Load())), keyword(arg='backend', value=Constant(value='multiprocessing')), keyword(arg='verbose', value=Constant(value=11))]), args=[GeneratorExp(elt=Call(func=Call(func=Name(id='delayed', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_forecast_pipeline', ctx=Load())], keywords=[]), args=[], keywords=[keyword(arg='pipeline', value=Name(id='pipeline', ctx=Load()))]), generators=[comprehension(target=Name(id='pipeline', ctx=Store()), iter=Attribute(value=Name(id='self', ctx=Load()), attr='pipelines', ctx=Load()), ifs=[], is_async=0)])], keywords=[])), Assign(targets=[Name(id='forecast', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_merge', ctx=Load()), args=[], keywords=[keyword(arg='forecasts', value=Name(id='forecasts', ctx=Load()))])), Return(value=Name(id='forecast', ctx=Load()))], decorator_list=[], returns=Name(id='TSDataset', ctx=Load())), FunctionDef(name='_predict', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Name(id='TSDataset', ctx=Load())), arg(arg='start_timestamp', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load())), arg(arg='end_timestamp', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='Timestamp', ctx=Load())), arg(arg='prediction_interval', annotation=Name(id='bool', ctx=Load())), arg(arg='quantiles', annotation=Subscript(value=Name(id='Sequence', ctx=Load()), slice=Name(id='float', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Name(id='prediction_interval', ctx=Load()), body=[Raise(exc=Call(func=Name(id='NotImplementedError', ctx=Load()), args=[JoinedStr(values=[Constant(value='Ensemble '), FormattedValue(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='__class__', ctx=Load()), attr='__name__', ctx=Load()), conversion=-1), Constant(value=" doesn't support prediction intervals!")])], keywords=[]))], orelse=[]), Assign(targets=[Name(id='horizons', ctx=Store())], value=ListComp(elt=Attribute(value=Name(id='pipeline', ctx=Load()), attr='horizon', ctx=Load()), generators=[comprehension(target=Name(id='pipeline', ctx=Store()), iter=Attribute(value=Name(id='self', ctx=Load()), attr='pipelines', ctx=Load()), ifs=[], is_async=0)])), Assign(targets=[Name(id='pipeline', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='pipelines', ctx=Load()), slice=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='argmin', ctx=Load()), args=[Name(id='horizons', ctx=Load())], keywords=[]), ctx=Load())), Assign(targets=[Name(id='prediction', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_predict_pipeline', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load())), keyword(arg='pipeline', value=Name(id='pipeline', ctx=Load())), keyword(arg='start_timestamp', value=Name(id='start_timestamp', ctx=Load())), keyword(arg='end_timestamp', value=Name(id='end_timestamp', ctx=Load()))])), Return(value=Name(id='prediction', ctx=Load()))], decorator_list=[], returns=Name(id='TSDataset', ctx=Load()))], decorator_list=[])], type_ignores=[])
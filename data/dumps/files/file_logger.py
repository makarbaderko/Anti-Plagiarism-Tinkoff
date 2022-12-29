Module(body=[Import(names=[alias(name='datetime')]), Import(names=[alias(name='json')]), Import(names=[alias(name='os')]), Import(names=[alias(name='pathlib')]), Import(names=[alias(name='tempfile')]), Import(names=[alias(name='warnings')]), ImportFrom(module='abc', names=[alias(name='abstractmethod')], level=0), ImportFrom(module='copy', names=[alias(name='copy')], level=0), ImportFrom(module='typing', names=[alias(name='TYPE_CHECKING')], level=0), ImportFrom(module='typing', names=[alias(name='Any')], level=0), ImportFrom(module='typing', names=[alias(name='Dict')], level=0), ImportFrom(module='typing', names=[alias(name='Optional')], level=0), ImportFrom(module='typing', names=[alias(name='Union')], level=0), Import(names=[alias(name='boto3')]), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='botocore.exceptions', names=[alias(name='ClientError')], level=0), ImportFrom(module='etna.loggers.base', names=[alias(name='BaseLogger')], level=0), If(test=Name(id='TYPE_CHECKING', ctx=Load()), body=[ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0)], orelse=[]), Assign(targets=[Name(id='DATETIME_FORMAT', ctx=Store())], value=Constant(value='%Y-%m-%dT%H-%M-%S')), ClassDef(name='BaseFileLogger', bases=[Name(id='BaseLogger', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Base logger for logging files.')), FunctionDef(name='log', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='msg', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='Any', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='kwargs'), defaults=[]), body=[Expr(value=Constant(value='\n        Log any event.\n\n        This class does nothing with it, use other loggers to do it.\n\n        Parameters\n        ----------\n        msg:\n            Message or dict to log\n        kwargs:\n            Additional parameters for particular implementation\n        ')), Pass()], decorator_list=[]), FunctionDef(name='_save_table', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='table', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='name', annotation=Name(id='str', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Save table with given name.\n\n        Parameters\n        ----------\n        table:\n            dataframe to save\n        name:\n            filename without extensions\n        ')), Pass()], decorator_list=[Name(id='abstractmethod', ctx=Load())]), FunctionDef(name='_save_dict', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='dictionary', annotation=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='Any', ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='name', annotation=Name(id='str', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Save dictionary with given name.\n\n        Parameters\n        ----------\n        dictionary:\n            dict to save\n        name:\n            filename without extensions\n        ')), Pass()], decorator_list=[Name(id='abstractmethod', ctx=Load())]), FunctionDef(name='_save_config', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='config', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='Any', ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Save config during init.\n\n        Parameters\n        ----------\n        config:\n            a dictionary-like object for saving inputs to your job,\n            like hyperparameters for a model or settings for a data preprocessing job\n        ')), If(test=Compare(left=Name(id='config', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='start_experiment', ctx=Load()), args=[], keywords=[])), Try(body=[Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_save_dict', ctx=Load()), args=[Name(id='config', ctx=Load()), Constant(value='config')], keywords=[]))], handlers=[ExceptHandler(type=Name(id='Exception', ctx=Load()), name='e', body=[Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='warn', ctx=Load()), args=[Call(func=Name(id='str', ctx=Load()), args=[Name(id='e', ctx=Load())], keywords=[]), Name(id='UserWarning', ctx=Load())], keywords=[]))])], orelse=[], finalbody=[])], orelse=[])], decorator_list=[]), FunctionDef(name='start_experiment', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='job_type', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), arg(arg='group', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()))], vararg=arg(arg='args'), kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='kwargs'), defaults=[Constant(value=None), Constant(value=None)]), body=[Expr(value=Constant(value="Start experiment within current experiment, it is used for separate different folds during backtest.\n\n        Parameters\n        ----------\n        job_type:\n            Specify the type of run, which is useful when you're grouping runs together\n            into larger experiments using group.\n        group:\n            Specify a group to organize individual runs into a larger experiment.\n        ")), Pass()], decorator_list=[Name(id='abstractmethod', ctx=Load())]), FunctionDef(name='log_backtest_run', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='metrics', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='forecast', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='test', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\n        Backtest metrics from one fold to logger.\n\n        Parameters\n        ----------\n        metrics:\n            Dataframe with metrics from backtest fold\n        forecast:\n            Dataframe with forecast\n        test:\n            Dataframe with ground truth\n\n        Notes\n        -----\n        If some exception during saving is raised, then it becomes a warning.\n        ')), ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0), ImportFrom(module='etna.metrics.utils', names=[alias(name='aggregate_metrics_df')], level=0), Assign(targets=[Name(id='columns_name', ctx=Store())], value=Call(func=Name(id='list', ctx=Load()), args=[Attribute(value=Name(id='metrics', ctx=Load()), attr='columns', ctx=Load())], keywords=[])), Assign(targets=[Name(id='metrics', ctx=Store())], value=Call(func=Attribute(value=Name(id='metrics', ctx=Load()), attr='reset_index', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='metrics', ctx=Load()), attr='columns', ctx=Store())], value=BinOp(left=List(elts=[Constant(value='segment')], ctx=Load()), op=Add(), right=Name(id='columns_name', ctx=Load()))), Try(body=[Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_save_table', ctx=Load()), args=[Name(id='metrics', ctx=Load()), Constant(value='metrics')], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_save_table', ctx=Load()), args=[Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_flatten', ctx=Load()), args=[Name(id='forecast', ctx=Load())], keywords=[]), Constant(value='forecast')], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_save_table', ctx=Load()), args=[Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_flatten', ctx=Load()), args=[Name(id='test', ctx=Load())], keywords=[]), Constant(value='test')], keywords=[]))], handlers=[ExceptHandler(type=Name(id='Exception', ctx=Load()), name='e', body=[Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='warn', ctx=Load()), args=[Call(func=Name(id='str', ctx=Load()), args=[Name(id='e', ctx=Load())], keywords=[]), Name(id='UserWarning', ctx=Load())], keywords=[]))])], orelse=[], finalbody=[]), Assign(targets=[Name(id='metrics_dict', ctx=Store())], value=Call(func=Name(id='aggregate_metrics_df', ctx=Load()), args=[Name(id='metrics', ctx=Load())], keywords=[])), Try(body=[Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_save_dict', ctx=Load()), args=[Name(id='metrics_dict', ctx=Load()), Constant(value='metrics_summary')], keywords=[]))], handlers=[ExceptHandler(type=Name(id='Exception', ctx=Load()), name='e', body=[Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='warn', ctx=Load()), args=[Call(func=Name(id='str', ctx=Load()), args=[Name(id='e', ctx=Load())], keywords=[]), Name(id='UserWarning', ctx=Load())], keywords=[]))])], orelse=[], finalbody=[])], decorator_list=[]), FunctionDef(name='log_backtest_metrics', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Constant(value='TSDataset')), arg(arg='metrics_df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='forecast_df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='fold_info_df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='\n        Write metrics to logger.\n\n        Parameters\n        ----------\n        ts:\n            TSDataset to with backtest data\n        metrics_df:\n            Dataframe produced with :py:meth:`etna.pipeline.Pipeline._get_backtest_metrics`\n        forecast_df:\n            Forecast from backtest\n        fold_info_df:\n            Fold information from backtest\n\n        Notes\n        -----\n        If some exception during saving is raised, then it becomes a warning.\n        ')), ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0), ImportFrom(module='etna.metrics.utils', names=[alias(name='aggregate_metrics_df')], level=0), Try(body=[Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_save_table', ctx=Load()), args=[Name(id='metrics_df', ctx=Load()), Constant(value='metrics')], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_save_table', ctx=Load()), args=[Call(func=Attribute(value=Name(id='TSDataset', ctx=Load()), attr='to_flatten', ctx=Load()), args=[Name(id='forecast_df', ctx=Load())], keywords=[]), Constant(value='forecast')], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_save_table', ctx=Load()), args=[Name(id='fold_info_df', ctx=Load()), Constant(value='fold_info')], keywords=[]))], handlers=[ExceptHandler(type=Name(id='Exception', ctx=Load()), name='e', body=[Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='warn', ctx=Load()), args=[Call(func=Name(id='str', ctx=Load()), args=[Name(id='e', ctx=Load())], keywords=[]), Name(id='UserWarning', ctx=Load())], keywords=[]))])], orelse=[], finalbody=[]), Assign(targets=[Name(id='metrics_dict', ctx=Store())], value=Call(func=Name(id='aggregate_metrics_df', ctx=Load()), args=[Name(id='metrics_df', ctx=Load())], keywords=[])), Try(body=[Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_save_dict', ctx=Load()), args=[Name(id='metrics_dict', ctx=Load()), Constant(value='metrics_summary')], keywords=[]))], handlers=[ExceptHandler(type=Name(id='Exception', ctx=Load()), name='e', body=[Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='warn', ctx=Load()), args=[Call(func=Name(id='str', ctx=Load()), args=[Name(id='e', ctx=Load())], keywords=[]), Name(id='UserWarning', ctx=Load())], keywords=[]))])], orelse=[], finalbody=[])], decorator_list=[])], decorator_list=[]), ClassDef(name='LocalFileLogger', bases=[Name(id='BaseFileLogger', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Logger for logging files into local folder.\n\n    It writes its result into folder like ``experiments_folder/2021-12-12T12-12-12``, where the second part\n    is related to datetime of starting the experiment.\n\n    After every ``start_experiment`` it creates a new subfolder ``job_type/group``.\n    If some of these two values are None then behaviour is little different and described in ``start_experiment`` method.\n    ')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='experiments_folder', annotation=Name(id='str', ctx=Load())), arg(arg='config', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='Any', ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load())), arg(arg='gzip', annotation=Name(id='bool', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None), Constant(value=False)]), body=[Expr(value=Constant(value='\n        Create instance of LocalFileLogger.\n\n        Parameters\n        ----------\n        experiments_folder:\n            path to folder to create experiment in\n        config:\n            a dictionary-like object for saving inputs to your job,\n            like hyperparameters for a model or settings for a data preprocessing job\n        gzip:\n            indicator whether to use compression during saving tables or not\n        ')), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='experiments_folder', ctx=Store())], value=Name(id='experiments_folder', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='config', ctx=Store())], value=Name(id='config', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='gzip', ctx=Store())], value=Name(id='gzip', ctx=Load())), Assign(targets=[Name(id='cur_datetime', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='datetime', ctx=Load()), attr='datetime', ctx=Load()), attr='now', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='subfolder_name', ctx=Store())], value=Call(func=Attribute(value=Name(id='cur_datetime', ctx=Load()), attr='strftime', ctx=Load()), args=[Name(id='DATETIME_FORMAT', ctx=Load())], keywords=[])), Assign(targets=[Name(id='experiments_folder_path', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='pathlib', ctx=Load()), attr='Path', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='experiments_folder', ctx=Load())], keywords=[]), attr='resolve', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='experiments_folder_path', ctx=Load()), attr='mkdir', ctx=Load()), args=[], keywords=[keyword(arg='exist_ok', value=Constant(value=True))])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='experiment_folder', ctx=Store())], value=Call(func=Attribute(value=Name(id='experiments_folder_path', ctx=Load()), attr='joinpath', ctx=Load()), args=[Name(id='subfolder_name', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='experiment_folder', ctx=Load()), attr='mkdir', ctx=Load()), args=[], keywords=[])), AnnAssign(target=Attribute(value=Name(id='self', ctx=Load()), attr='_current_experiment_folder', ctx=Store()), annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Attribute(value=Name(id='pathlib', ctx=Load()), attr='Path', ctx=Load()), ctx=Load()), value=Constant(value=None), simple=0), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_save_config', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='config', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='start_experiment', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='job_type', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), arg(arg='group', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()))], vararg=arg(arg='args'), kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='kwargs'), defaults=[Constant(value=None), Constant(value=None)]), body=[Expr(value=Constant(value="Start experiment within current experiment, it is used for separate different folds during backtest.\n\n        As a result, within ``self.experiment_folder`` subfolder ``job_type/group`` is created.\n\n        * If ``job_type`` or ``group`` isn't set then only one-level subfolder is created.\n\n        * If none of ``job_type`` and ``group`` is set then experiment logs files into ``self.experiment_folder``.\n\n        Parameters\n        ----------\n        job_type:\n            Specify the type of run, which is useful when you're grouping runs together\n            into larger experiments using group.\n        group:\n            Specify a group to organize individual runs into a larger experiment.\n        ")), If(test=BoolOp(op=And(), values=[Compare(left=Name(id='job_type', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), Compare(left=Name(id='group', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)])]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_current_experiment_folder', ctx=Store())], value=Call(func=Name(id='copy', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='experiment_folder', ctx=Load())], keywords=[])), Return()], orelse=[If(test=BoolOp(op=And(), values=[Compare(left=Name(id='job_type', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), Compare(left=Name(id='group', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)])]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_current_experiment_folder', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='experiment_folder', ctx=Load()), attr='joinpath', ctx=Load()), args=[Name(id='group', ctx=Load())], keywords=[]))], orelse=[If(test=BoolOp(op=And(), values=[Compare(left=Name(id='job_type', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), Compare(left=Name(id='group', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)])]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_current_experiment_folder', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='experiment_folder', ctx=Load()), attr='joinpath', ctx=Load()), args=[Name(id='job_type', ctx=Load())], keywords=[]))], orelse=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_current_experiment_folder', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='experiment_folder', ctx=Load()), attr='joinpath', ctx=Load()), args=[Name(id='job_type', ctx=Load())], keywords=[]), attr='joinpath', ctx=Load()), args=[Name(id='group', ctx=Load())], keywords=[]))])])]), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_current_experiment_folder', ctx=Load()), attr='mkdir', ctx=Load()), args=[], keywords=[keyword(arg='parents', value=Constant(value=True))]))], decorator_list=[]), FunctionDef(name='_save_table', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='table', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='name', annotation=Name(id='str', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Save table with given name.\n\n        Parameters\n        ----------\n        table:\n            dataframe to save\n        name:\n            filename without extensions\n        ')), If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_current_experiment_folder', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='You should start experiment before using log_backtest_run or log_backtest_metrics')], keywords=[]))], orelse=[]), If(test=Attribute(value=Name(id='self', ctx=Load()), attr='gzip', ctx=Load()), body=[Assign(targets=[Name(id='filename', ctx=Store())], value=JoinedStr(values=[FormattedValue(value=Name(id='name', ctx=Load()), conversion=-1), Constant(value='.csv.gz')])), Expr(value=Call(func=Attribute(value=Name(id='table', ctx=Load()), attr='to_csv', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_current_experiment_folder', ctx=Load()), attr='joinpath', ctx=Load()), args=[Name(id='filename', ctx=Load())], keywords=[])], keywords=[keyword(arg='index', value=Constant(value=False)), keyword(arg='compression', value=Constant(value='gzip'))]))], orelse=[Assign(targets=[Name(id='filename', ctx=Store())], value=JoinedStr(values=[FormattedValue(value=Name(id='name', ctx=Load()), conversion=-1), Constant(value='.csv')])), Expr(value=Call(func=Attribute(value=Name(id='table', ctx=Load()), attr='to_csv', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_current_experiment_folder', ctx=Load()), attr='joinpath', ctx=Load()), args=[Name(id='filename', ctx=Load())], keywords=[])], keywords=[keyword(arg='index', value=Constant(value=False))]))])], decorator_list=[]), FunctionDef(name='_save_dict', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='dictionary', annotation=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='Any', ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='name', annotation=Name(id='str', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Save dictionary with given name.\n\n        Parameters\n        ----------\n        dictionary:\n            dict to save\n        name:\n            filename without extensions\n        ')), If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_current_experiment_folder', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='You should start experiment before using log_backtest_run or log_backtest_metrics')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='filename', ctx=Store())], value=JoinedStr(values=[FormattedValue(value=Name(id='name', ctx=Load()), conversion=-1), Constant(value='.json')])), With(items=[withitem(context_expr=Call(func=Name(id='open', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_current_experiment_folder', ctx=Load()), attr='joinpath', ctx=Load()), args=[Name(id='filename', ctx=Load())], keywords=[]), Constant(value='w')], keywords=[]), optional_vars=Name(id='ouf', ctx=Store()))], body=[Expr(value=Call(func=Attribute(value=Name(id='json', ctx=Load()), attr='dump', ctx=Load()), args=[Name(id='dictionary', ctx=Load()), Name(id='ouf', ctx=Load())], keywords=[]))])], decorator_list=[])], decorator_list=[]), ClassDef(name='S3FileLogger', bases=[Name(id='BaseFileLogger', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Logger for logging files into S3 bucket.\n\n    This logger is very similar to :class:`~etna.loggers.file_logger.LocalFileLogger`,\n    but works with S3 keys instead of paths at local file system.\n    ')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='bucket', annotation=Name(id='str', ctx=Load())), arg(arg='experiments_folder', annotation=Name(id='str', ctx=Load())), arg(arg='config', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='Any', ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load())), arg(arg='gzip', annotation=Name(id='bool', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None), Constant(value=False)]), body=[Expr(value=Constant(value="\n        Create instance of S3FileLogger.\n\n        Parameters\n        ----------\n        bucket:\n            name of the S3 bucket\n        experiments_folder:\n            path to folder to create experiment in\n        config:\n            a dictionary-like object for saving inputs to your job,\n            like hyperparameters for a model or settings for a data preprocessing job\n        gzip:\n            indicator whether to use compression during saving tables or not\n\n\n        Raises\n        ------\n        ValueError:\n            if environment variable ``endpoint_url`` isn't set\n        ValueError:\n            if environment variable ``aws_access_key_id`` isn't set\n        ValueError:\n            if environment variable ``aws_secret_access_key`` isn't set\n        ValueError:\n            if bucket doesn't exist\n        ")), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='bucket', ctx=Store())], value=Name(id='bucket', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='experiments_folder', ctx=Store())], value=Name(id='experiments_folder', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='config', ctx=Store())], value=Name(id='config', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='s3_client', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_s3_client', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='gzip', ctx=Store())], value=Name(id='gzip', ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_check_bucket', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='cur_datetime', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='datetime', ctx=Load()), attr='datetime', ctx=Load()), attr='now', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='subfolder_name', ctx=Store())], value=Call(func=Attribute(value=Name(id='cur_datetime', ctx=Load()), attr='strftime', ctx=Load()), args=[Name(id='DATETIME_FORMAT', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='experiment_folder', ctx=Store())], value=JoinedStr(values=[FormattedValue(value=Name(id='experiments_folder', ctx=Load()), conversion=-1), Constant(value='/'), FormattedValue(value=Name(id='subfolder_name', ctx=Load()), conversion=-1)])), AnnAssign(target=Attribute(value=Name(id='self', ctx=Load()), attr='_current_experiment_folder', ctx=Store()), annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()), value=Constant(value=None), simple=0), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_save_config', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='config', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='_check_bucket', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Try(body=[Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='s3_client', ctx=Load()), attr='head_bucket', ctx=Load()), args=[], keywords=[keyword(arg='Bucket', value=Attribute(value=Name(id='self', ctx=Load()), attr='bucket', ctx=Load()))]))], handlers=[ExceptHandler(type=Name(id='ClientError', ctx=Load()), name='e', body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[JoinedStr(values=[Constant(value='Error occurred during checking bucket: '), FormattedValue(value=Call(func=Name(id='str', ctx=Load()), args=[Name(id='e', ctx=Load())], keywords=[]), conversion=-1)])], keywords=[]))])], orelse=[], finalbody=[])], decorator_list=[]), FunctionDef(name='_get_s3_client', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='endpoint_url', ctx=Store())], value=Call(func=Attribute(value=Name(id='os', ctx=Load()), attr='getenv', ctx=Load()), args=[Constant(value='endpoint_url')], keywords=[])), If(test=Compare(left=Name(id='endpoint_url', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='OSError', ctx=Load()), args=[Constant(value='Environment variable `endpoint_url` should be specified for using this class')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='aws_access_key_id', ctx=Store())], value=Call(func=Attribute(value=Name(id='os', ctx=Load()), attr='getenv', ctx=Load()), args=[Constant(value='aws_access_key_id')], keywords=[])), If(test=Compare(left=Name(id='aws_access_key_id', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='OSError', ctx=Load()), args=[Constant(value='Environment variable `aws_access_key_id` should be specified for using this class')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='aws_secret_access_key', ctx=Store())], value=Call(func=Attribute(value=Name(id='os', ctx=Load()), attr='getenv', ctx=Load()), args=[Constant(value='aws_secret_access_key')], keywords=[])), If(test=Compare(left=Name(id='aws_secret_access_key', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='OSError', ctx=Load()), args=[Constant(value='Environment variable `aws_secret_access_key` should be specified for using this class')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='s3_client', ctx=Store())], value=Call(func=Attribute(value=Name(id='boto3', ctx=Load()), attr='client', ctx=Load()), args=[Constant(value='s3')], keywords=[keyword(arg='endpoint_url', value=Name(id='endpoint_url', ctx=Load())), keyword(arg='aws_access_key_id', value=Name(id='aws_access_key_id', ctx=Load())), keyword(arg='aws_secret_access_key', value=Name(id='aws_secret_access_key', ctx=Load()))])), Return(value=Name(id='s3_client', ctx=Load()))], decorator_list=[Name(id='staticmethod', ctx=Load())]), FunctionDef(name='start_experiment', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='job_type', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), arg(arg='group', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()))], vararg=arg(arg='args'), kwonlyargs=[], kw_defaults=[], kwarg=arg(arg='kwargs'), defaults=[Constant(value=None), Constant(value=None)]), body=[Expr(value=Constant(value="Start experiment within current experiment, it is used for separate different folds during backtest.\n\n        As a result, ``self.experiment_folder`` key is extended with ``job_type/group``.\n\n        * If ``job_type`` or ``group`` isn't set then key is extended with one value.\n\n        * If none of ``job_type`` and ``group`` is set then ``self.experiment_folder`` is not extended.\n\n        Parameters\n        ----------\n        job_type:\n            Specify the type of run, which is useful when you're grouping runs together\n            into larger experiments using group.\n        group:\n            Specify a group to organize individual runs into a larger experiment.\n        ")), If(test=BoolOp(op=And(), values=[Compare(left=Name(id='job_type', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), Compare(left=Name(id='group', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)])]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_current_experiment_folder', ctx=Store())], value=Call(func=Name(id='copy', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='experiment_folder', ctx=Load())], keywords=[]))], orelse=[If(test=Compare(left=Name(id='job_type', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_current_experiment_folder', ctx=Store())], value=JoinedStr(values=[FormattedValue(value=Attribute(value=Name(id='self', ctx=Load()), attr='experiment_folder', ctx=Load()), conversion=-1), Constant(value='/'), FormattedValue(value=Name(id='group', ctx=Load()), conversion=-1)]))], orelse=[If(test=Compare(left=Name(id='group', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_current_experiment_folder', ctx=Store())], value=JoinedStr(values=[FormattedValue(value=Attribute(value=Name(id='self', ctx=Load()), attr='experiment_folder', ctx=Load()), conversion=-1), Constant(value='/'), FormattedValue(value=Name(id='job_type', ctx=Load()), conversion=-1)]))], orelse=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_current_experiment_folder', ctx=Store())], value=JoinedStr(values=[FormattedValue(value=Attribute(value=Name(id='self', ctx=Load()), attr='experiment_folder', ctx=Load()), conversion=-1), Constant(value='/'), FormattedValue(value=Name(id='job_type', ctx=Load()), conversion=-1), Constant(value='/'), FormattedValue(value=Name(id='group', ctx=Load()), conversion=-1)]))])])])], decorator_list=[]), FunctionDef(name='_save_table', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='table', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), arg(arg='name', annotation=Name(id='str', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Save table with given name.\n\n        Parameters\n        ----------\n        table:\n            dataframe to save\n        name:\n            filename without extensions\n        ')), If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_current_experiment_folder', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='You should start experiment before using log_backtest_run or log_backtest_metrics')], keywords=[]))], orelse=[]), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='tempfile', ctx=Load()), attr='NamedTemporaryFile', ctx=Load()), args=[], keywords=[]), optional_vars=Name(id='ouf', ctx=Store()))], body=[If(test=Attribute(value=Name(id='self', ctx=Load()), attr='gzip', ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Name(id='table', ctx=Load()), attr='to_csv', ctx=Load()), args=[Attribute(value=Name(id='ouf', ctx=Load()), attr='name', ctx=Load())], keywords=[keyword(arg='index', value=Constant(value=False)), keyword(arg='compression', value=Constant(value='gzip'))])), Assign(targets=[Name(id='filename', ctx=Store())], value=JoinedStr(values=[FormattedValue(value=Name(id='name', ctx=Load()), conversion=-1), Constant(value='.csv.gz')]))], orelse=[Expr(value=Call(func=Attribute(value=Name(id='table', ctx=Load()), attr='to_csv', ctx=Load()), args=[Attribute(value=Name(id='ouf', ctx=Load()), attr='name', ctx=Load())], keywords=[keyword(arg='index', value=Constant(value=False))])), Assign(targets=[Name(id='filename', ctx=Store())], value=JoinedStr(values=[FormattedValue(value=Name(id='name', ctx=Load()), conversion=-1), Constant(value='.csv')]))]), Assign(targets=[Name(id='key', ctx=Store())], value=JoinedStr(values=[FormattedValue(value=Attribute(value=Name(id='self', ctx=Load()), attr='_current_experiment_folder', ctx=Load()), conversion=-1), Constant(value='/'), FormattedValue(value=Name(id='filename', ctx=Load()), conversion=-1)])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='s3_client', ctx=Load()), attr='upload_file', ctx=Load()), args=[], keywords=[keyword(arg='Bucket', value=Attribute(value=Name(id='self', ctx=Load()), attr='bucket', ctx=Load())), keyword(arg='Key', value=Name(id='key', ctx=Load())), keyword(arg='Filename', value=Attribute(value=Name(id='ouf', ctx=Load()), attr='name', ctx=Load()))]))])], decorator_list=[]), FunctionDef(name='_save_dict', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='dictionary', annotation=Subscript(value=Name(id='Dict', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Name(id='Any', ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='name', annotation=Name(id='str', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Save dictionary with given name.\n\n        Parameters\n        ----------\n        dictionary:\n            dict to save\n        name:\n            filename without extensions\n        ')), If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_current_experiment_folder', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='You should start experiment before using log_backtest_run or log_backtest_metrics')], keywords=[]))], orelse=[]), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='tempfile', ctx=Load()), attr='NamedTemporaryFile', ctx=Load()), args=[], keywords=[keyword(arg='mode', value=Constant(value='w+'))]), optional_vars=Name(id='ouf', ctx=Store()))], body=[Expr(value=Call(func=Attribute(value=Name(id='json', ctx=Load()), attr='dump', ctx=Load()), args=[Name(id='dictionary', ctx=Load()), Name(id='ouf', ctx=Load())], keywords=[])), Assign(targets=[Name(id='filename', ctx=Store())], value=JoinedStr(values=[FormattedValue(value=Name(id='name', ctx=Load()), conversion=-1), Constant(value='.json')])), Expr(value=Call(func=Attribute(value=Name(id='ouf', ctx=Load()), attr='flush', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='key', ctx=Store())], value=JoinedStr(values=[FormattedValue(value=Attribute(value=Name(id='self', ctx=Load()), attr='_current_experiment_folder', ctx=Load()), conversion=-1), Constant(value='/'), FormattedValue(value=Name(id='filename', ctx=Load()), conversion=-1)])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='s3_client', ctx=Load()), attr='upload_file', ctx=Load()), args=[], keywords=[keyword(arg='Bucket', value=Attribute(value=Name(id='self', ctx=Load()), attr='bucket', ctx=Load())), keyword(arg='Key', value=Name(id='key', ctx=Load())), keyword(arg='Filename', value=Attribute(value=Name(id='ouf', ctx=Load()), attr='name', ctx=Load()))]))])], decorator_list=[])], decorator_list=[])], type_ignores=[])
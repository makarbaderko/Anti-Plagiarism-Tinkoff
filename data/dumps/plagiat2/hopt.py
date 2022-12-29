Module(body=[ImportFrom(module='config', names=[alias(name='has_hopts'), alias(name='as_flat_config'), alias(name='as_nested_config'), alias(name='CONFIG_HOPT'), alias(name='ConfigError')], level=2), Import(names=[alias(name='os')]), Import(names=[alias(name='math')]), ImportFrom(module='collections', names=[alias(name='OrderedDict')], level=0), Import(names=[alias(name='shutil')]), Import(names=[alias(name='sys')]), Import(names=[alias(name='tempfile')]), Import(names=[alias(name='traceback')]), ImportFrom(module='common', names=[alias(name='make_directory')], level=1), Import(names=[alias(name='optuna')]), Import(names=[alias(name='wandb')]), ImportFrom(module='config', names=[alias(name='read_config'), alias(name='write_config'), alias(name='prepare_config'), alias(name='update_config')], level=2), ImportFrom(module='cval', names=[alias(name='cval')], level=1), ImportFrom(module='runner', names=[alias(name='Runner'), alias(name='parse_logger')], level=2), Import(names=[alias(name='copy')]), ImportFrom(module='basic', names=[alias(name='train')], level=1), Import(names=[alias(name='random')]), ImportFrom(module='trainer', names=[alias(name='Trainer')], level=2), FunctionDef(name='patch_logger', args=arguments(posonlyargs=[], args=[arg(arg='logger'), arg(arg='l'), arg(arg='run_id')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='           ')), Assign(targets=[Tuple(elts=[Name(id='LOGGER_TYPE', ctx=Store()), Name(id='PROJECT', ctx=Store()), Name(id='experiment', ctx=Store()), Name(id='groupUbeuj', ctx=Store())], ctx=Store())], value=Call(func=Name(id='parse_logger', ctx=Load()), args=[Name(id='logger', ctx=Load())], keywords=[])), If(test=Compare(left=Name(id='LOGGER_TYPE', ctx=Load()), ops=[Eq()], comparators=[Constant(value='tensorboard')]), body=[Return(value=Name(id='logger', ctx=Load()))], orelse=[If(test=Compare(left=Name(id='LOGGER_TYPE', ctx=Load()), ops=[NotEq()], comparators=[Constant(value='wandb')]), body=[Raise(exc=Call(func=Name(id='ValueErrorWT', ctx=Load()), args=[Call(func=Attribute(value=Constant(value='Unknown logger: {}'), attr='format', ctx=Load()), args=[Name(id='LOGGER_TYPE', ctx=Load())], keywords=[])], keywords=[]))], orelse=[])]), If(test=Compare(left=Name(id='groupUbeuj', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Assign(targets=[Name(id='groupUbeuj', ctx=Store())], value=BinOp(left=BinOp(left=Name(id='experiment', ctx=Load()), op=Add(), right=Constant(value='-')), op=Add(), right=Name(id='l', ctx=Load())))], orelse=[]), Assign(targets=[Name(id='experiment', ctx=Store())], value=BinOp(left=BinOp(left=BinOp(left=BinOp(left=Name(id='experiment', ctx=Load()), op=Add(), right=Constant(value='-')), op=Add(), right=Name(id='l', ctx=Load())), op=Add(), right=Constant(value='-')), op=Add(), right=Name(id='run_id', ctx=Load()))), Assign(targets=[Name(id='logger', ctx=Store())], value=Call(func=Attribute(value=Constant(value=':'), attr='join', ctx=Load()), args=[List(elts=[Name(id='LOGGER_TYPE', ctx=Load()), Name(id='PROJECT', ctx=Load()), Name(id='experiment', ctx=Load()), Name(id='groupUbeuj', ctx=Load())], ctx=Load())], keywords=[])), Return(value=Name(id='logger', ctx=Load()))], decorator_list=[]), FunctionDef(name='make_sweep', args=arguments(posonlyargs=[], args=[arg(arg='PROJECT'), arg(arg='experiment'), arg(arg='config_path')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='             ǁ       ')), Assign(targets=[Name(id='con_fig', ctx=Store())], value=Call(func=Name(id='read_config', ctx=Load()), args=[Name(id='config_path', ctx=Load())], keywords=[])), If(test=UnaryOp(op=Not(), operand=Call(func=Name(id='has_hopts', ctx=Load()), args=[Name(id='con_fig', ctx=Load())], keywords=[])), body=[Raise(exc=Call(func=Name(id='runtimeerror', ctx=Load()), args=[Constant(value='No hyper parameters to optimize')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='ru_nner_config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='Runner', ctx=Load()), Name(id='con_fig', ctx=Load())], keywords=[])), Assign(targets=[Name(id='trainer_config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='Trainer', ctx=Load()), Subscript(value=Name(id='con_fig', ctx=Load()), slice=Constant(value='trainer_params'), ctx=Load())], keywords=[])), Assign(targets=[Name(id='flat_conf', ctx=Store())], value=Call(func=Name(id='as_flat_config', ctx=Load()), args=[Name(id='con_fig', ctx=Load())], keywords=[])), Assign(targets=[Name(id='flat_hopts', ctx=Store())], value=Call(func=Attribute(value=Name(id='flat_conf', ctx=Load()), attr='pop', ctx=Load()), args=[Name(id='CONFIG_HOPT', ctx=Load())], keywords=[])), Assign(targets=[Name(id='flat_conf', ctx=Store())], value=DictComp(key=Name(id='k', ctx=Load()), value=Dict(keys=[Constant(value='value')], values=[Name(id='v', ctx=Load())]), generators=[comprehension(target=Tuple(elts=[Name(id='k', ctx=Store()), Name(id='v', ctx=Store())], ctx=Store()), iter=Call(func=Attribute(value=Name(id='flat_conf', ctx=Load()), attr='items', ctx=Load()), args=[], keywords=[]), ifs=[], is_async=0)])), Expr(value=Call(func=Attribute(value=Name(id='flat_conf', ctx=Load()), attr='update', ctx=Load()), args=[Name(id='flat_hopts', ctx=Load())], keywords=[])), Assign(targets=[Tuple(elts=[Name(id='_hopt_backend', ctx=Store()), Name(id='hopt', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Name(id='ru_nner_config', ctx=Load()), slice=Constant(value='hopt_backend'), ctx=Load()), attr='split', ctx=Load()), args=[Constant(value='-')], keywords=[])), Assert(test=Compare(left=Name(id='_hopt_backend', ctx=Load()), ops=[Eq()], comparators=[Constant(value='wandb')])), Assign(targets=[Name(id='sw_eep_config', ctx=Store())], value=Dict(keys=[Constant(value='name'), Constant(value='method'), Constant(value='early_terminate'), Constant(value='metric'), Constant(value='parameters')], values=[Name(id='experiment', ctx=Load()), Name(id='hopt', ctx=Load()), Dict(keys=[Constant(value='type'), Constant(value='min_iter'), Constant(value='eta')], values=[Constant(value='hyperband'), Subscript(value=Name(id='trainer_config', ctx=Load()), slice=Constant(value='early_stop_patience'), ctx=Load()), Subscript(value=Name(id='trainer_config', ctx=Load()), slice=Constant(value='early_stop_patience'), ctx=Load())]), Dict(keys=[Constant(value='name'), Constant(value='goal')], values=[Call(func=Attribute(value=Constant(value='{}_epoch/{}'), attr='format', ctx=Load()), args=[Subscript(value=Name(id='trainer_config', ctx=Load()), slice=Constant(value='selection_metric'), ctx=Load()), Subscript(value=Name(id='trainer_config', ctx=Load()), slice=Constant(value='selection_dataset'), ctx=Load())], keywords=[]), IfExp(test=Subscript(value=Name(id='trainer_config', ctx=Load()), slice=Constant(value='selection_minimize'), ctx=Load()), body=Constant(value='minimize'), orelse=Constant(value='maximize'))]), Call(func=Name(id='dictZ', ctx=Load()), args=[Name(id='flat_conf', ctx=Load())], keywords=[])])), Assign(targets=[Name(id='swee', ctx=Store())], value=Call(func=Attribute(value=Name(id='wandb', ctx=Load()), attr='sweep', ctx=Load()), args=[Name(id='sw_eep_config', ctx=Load())], keywords=[keyword(arg='project', value=Name(id='PROJECT', ctx=Load()))])), Return(value=Tuple(elts=[Name(id='swee', ctx=Load()), Subscript(value=Name(id='ru_nner_config', ctx=Load()), slice=Constant(value='num_hopt_trials'), ctx=Load())], ctx=Load()))], decorator_list=[]), ClassDef(name='HoptWorker', bases=[], keywords=[], body=[FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='selfVEe'), arg(arg='args'), arg(arg='l'), arg(arg='run_cvaldpDN')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ȫ  @ç    ð  ')), Assign(targets=[Attribute(value=Name(id='selfVEe', ctx=Load()), attr='_args', ctx=Store())], value=Name(id='args', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfVEe', ctx=Load()), attr='_logger_suffix', ctx=Store())], value=Name(id='l', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfVEe', ctx=Load()), attr='_run_cval', ctx=Store())], value=Name(id='run_cvaldpDN', ctx=Load()))], decorator_list=[]), FunctionDef(name='__call__', args=arguments(posonlyargs=[], args=[arg(arg='selfVEe'), arg(arg='optuna_')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None)]), body=[Try(body=[Return(value=Call(func=Attribute(value=Name(id='selfVEe', ctx=Load()), attr='run_worker', ctx=Load()), args=[Name(id='optuna_', ctx=Load())], keywords=[]))], handlers=[ExceptHandler(type=Name(id='Exception', ctx=Load()), body=[Expr(value=Call(func=Name(id='prin_t', ctx=Load()), args=[Call(func=Attribute(value=Name(id='traceback', ctx=Load()), attr='print_exc', ctx=Load()), args=[], keywords=[])], keywords=[keyword(arg='file', value=Attribute(value=Name(id='sys', ctx=Load()), attr='stderr', ctx=Load()))])), Expr(value=Call(func=Name(id='exit', ctx=Load()), args=[Constant(value=1)], keywords=[]))])], orelse=[], finalbody=[])], decorator_list=[]), FunctionDef(name='run_worker', args=arguments(posonlyargs=[], args=[arg(arg='selfVEe'), arg(arg='optuna_')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None)]), body=[Expr(value=Call(func=Attribute(value=Name(id='random', ctx=Load()), attr='seed', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='run_id', ctx=Store())], value=Call(func=Name(id='str', ctx=Load()), args=[Call(func=Attribute(value=Name(id='random', ctx=Load()), attr='randint', ctx=Load()), args=[Constant(value=0), Constant(value=1000000000000000.0)], keywords=[])], keywords=[])), Assign(targets=[Name(id='train_root', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Attribute(value=Attribute(value=Name(id='selfVEe', ctx=Load()), attr='_args', ctx=Load()), attr='train_root', ctx=Load()), Name(id='run_id', ctx=Load())], keywords=[])), Expr(value=Call(func=Name(id='make_directory', ctx=Load()), args=[Name(id='train_root', ctx=Load())], keywords=[])), Assign(targets=[Name(id='logger', ctx=Store())], value=Call(func=Name(id='patch_logger', ctx=Load()), args=[Attribute(value=Attribute(value=Name(id='selfVEe', ctx=Load()), attr='_args', ctx=Load()), attr='logger', ctx=Load()), Attribute(value=Name(id='selfVEe', ctx=Load()), attr='_logger_suffix', ctx=Load()), Name(id='run_id', ctx=Load())], keywords=[])), Assign(targets=[Tuple(elts=[Name(id='LOGGER_TYPE', ctx=Store()), Name(id='PROJECT', ctx=Store()), Name(id='experiment', ctx=Store()), Name(id='groupUbeuj', ctx=Store())], ctx=Store())], value=Call(func=Name(id='parse_logger', ctx=Load()), args=[Name(id='logger', ctx=Load())], keywords=[])), If(test=Compare(left=Name(id='optuna_', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Assign(targets=[Name(id='wandb_logge_r', ctx=Store())], value=Call(func=Attribute(value=Name(id='wandb', ctx=Load()), attr='init', ctx=Load()), args=[], keywords=[keyword(arg='project', value=Name(id='PROJECT', ctx=Load())), keyword(arg='name', value=Name(id='experiment', ctx=Load())), keyword(arg='group', value=Name(id='groupUbeuj', ctx=Load()))])), Assign(targets=[Name(id='fla', ctx=Store())], value=Call(func=Name(id='dictZ', ctx=Load()), args=[Attribute(value=Name(id='wandb_logge_r', ctx=Load()), attr='config', ctx=Load())], keywords=[])), Assign(targets=[Name(id='con_fig', ctx=Store())], value=Call(func=Name(id='as_nested_config', ctx=Load()), args=[Name(id='fla', ctx=Load())], keywords=[]))], orelse=[If(test=Compare(left=Name(id='LOGGER_TYPE', ctx=Load()), ops=[Eq()], comparators=[Constant(value='wandb')]), body=[Expr(value=Call(func=Attribute(value=Name(id='wandb', ctx=Load()), attr='init', ctx=Load()), args=[], keywords=[keyword(arg='project', value=Name(id='PROJECT', ctx=Load())), keyword(arg='name', value=Name(id='experiment', ctx=Load())), keyword(arg='group', value=Name(id='groupUbeuj', ctx=Load())), keyword(arg='reinit', value=Constant(value=True))]))], orelse=[]), Assign(targets=[Name(id='con_fig', ctx=Store())], value=Call(func=Name(id='read_config', ctx=Load()), args=[Attribute(value=Attribute(value=Name(id='selfVEe', ctx=Load()), attr='_args', ctx=Load()), attr='config', ctx=Load())], keywords=[])), Assign(targets=[Name(id='fla', ctx=Store())], value=Call(func=Name(id='as_flat_config', ctx=Load()), args=[Name(id='con_fig', ctx=Load())], keywords=[])), For(target=Tuple(elts=[Name(id='name_', ctx=Store()), Name(id='spe', ctx=Store())], ctx=Store()), iter=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='fla', ctx=Load()), attr='pop', ctx=Load()), args=[Name(id='CONFIG_HOPT', ctx=Load()), Dict(keys=[], values=[])], keywords=[]), attr='items', ctx=Load()), args=[], keywords=[]), body=[Assign(targets=[Subscript(value=Name(id='fla', ctx=Load()), slice=Name(id='name_', ctx=Load()), ctx=Store())], value=Call(func=Name(id='suggest', ctx=Load()), args=[Name(id='optuna_', ctx=Load()), Name(id='name_', ctx=Load()), Name(id='spe', ctx=Load())], keywords=[]))], orelse=[]), Assign(targets=[Name(id='con_fig', ctx=Store())], value=Call(func=Name(id='as_nested_config', ctx=Load()), args=[Name(id='fla', ctx=Load())], keywords=[]))]), Assign(targets=[Subscript(value=Name(id='con_fig', ctx=Load()), slice=Constant(value='seed'), ctx=Store())], value=Call(func=Attribute(value=Name(id='random', ctx=Load()), attr='randint', ctx=Load()), args=[Constant(value=0), BinOp(left=Constant(value=1), op=LShift(), right=Constant(value=16))], keywords=[])), Assign(targets=[Name(id='config_path', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='train_root', ctx=Load()), Constant(value='config.yaml')], keywords=[])), Expr(value=Call(func=Name(id='write_config', ctx=Load()), args=[Name(id='con_fig', ctx=Load()), Name(id='config_path', ctx=Load())], keywords=[])), Assign(targets=[Name(id='args', ctx=Store())], value=Call(func=Attribute(value=Name(id='copy', ctx=Load()), attr='copy', ctx=Load()), args=[Attribute(value=Name(id='selfVEe', ctx=Load()), attr='_args', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='args', ctx=Load()), attr='train_root', ctx=Store())], value=Name(id='train_root', ctx=Load())), Assign(targets=[Attribute(value=Name(id='args', ctx=Load()), attr='config', ctx=Store())], value=Name(id='config_path', ctx=Load())), Assign(targets=[Attribute(value=Name(id='args', ctx=Load()), attr='logger', ctx=Store())], value=Name(id='logger', ctx=Load())), If(test=Attribute(value=Name(id='selfVEe', ctx=Load()), attr='_run_cval', ctx=Load()), body=[Assign(targets=[Name(id='metrics', ctx=Store())], value=Call(func=Name(id='cval', ctx=Load()), args=[Name(id='args', ctx=Load())], keywords=[]))], orelse=[Assign(targets=[Name(id='metrics', ctx=Store())], value=Call(func=Name(id='train', ctx=Load()), args=[Name(id='args', ctx=Load())], keywords=[]))]), Assign(targets=[Name(id='trainer_config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='Trainer', ctx=Load()), Call(func=Attribute(value=Name(id='con_fig', ctx=Load()), attr='get', ctx=Load()), args=[Constant(value='trainer_params'), Constant(value=None)], keywords=[])], keywords=[])), Assign(targets=[Name(id='metr_ic', ctx=Store())], value=Subscript(value=Subscript(value=Name(id='metrics', ctx=Load()), slice=Subscript(value=Name(id='trainer_config', ctx=Load()), slice=Constant(value='selection_dataset'), ctx=Load()), ctx=Load()), slice=Subscript(value=Name(id='trainer_config', ctx=Load()), slice=Constant(value='selection_metric'), ctx=Load()), ctx=Load())), If(test=BoolOp(op=And(), values=[Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='metr_ic', ctx=Load()), Tuple(elts=[Name(id='dictZ', ctx=Load()), Name(id='OrderedDict', ctx=Load())], ctx=Load())], keywords=[]), Compare(left=Constant(value='mean'), ops=[In()], comparators=[Name(id='metr_ic', ctx=Load())])]), body=[Assign(targets=[Name(id='metr_ic', ctx=Store())], value=Subscript(value=Name(id='metr_ic', ctx=Load()), slice=Constant(value='mean'), ctx=Load()))], orelse=[]), If(test=Attribute(value=Name(id='args', ctx=Load()), attr='clean', ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Name(id='shutil', ctx=Load()), attr='rmtree', ctx=Load()), args=[Name(id='train_root', ctx=Load())], keywords=[]))], orelse=[]), Return(value=Call(func=Name(id='float', ctx=Load()), args=[Name(id='metr_ic', ctx=Load())], keywords=[]))], decorator_list=[])], decorator_list=[]), FunctionDef(name='hopt_optuna', args=arguments(posonlyargs=[], args=[arg(arg='args'), arg(arg='run_cvaldpDN')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=True)]), body=[Assign(targets=[Name(id='SAM', ctx=Store())], value=Dict(keys=[Constant(value='tpe')], values=[Attribute(value=Attribute(value=Name(id='optuna', ctx=Load()), attr='samplers', ctx=Load()), attr='TPESampler', ctx=Load())])), If(test=Compare(left=Attribute(value=Name(id='args', ctx=Load()), attr='sweep_id', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='ValueErrorWT', ctx=Load()), args=[Constant(value="Can't attach to sweep ID using Optuna.")], keywords=[]))], orelse=[]), Assign(targets=[Name(id='con_fig', ctx=Store())], value=IfExp(test=Compare(left=Attribute(value=Name(id='args', ctx=Load()), attr='config', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=Call(func=Name(id='read_config', ctx=Load()), args=[Attribute(value=Name(id='args', ctx=Load()), attr='config', ctx=Load())], keywords=[]), orelse=Dict(keys=[], values=[]))), If(test=UnaryOp(op=Not(), operand=Call(func=Name(id='has_hopts', ctx=Load()), args=[Name(id='con_fig', ctx=Load())], keywords=[])), body=[Raise(exc=Call(func=Name(id='runtimeerror', ctx=Load()), args=[Constant(value='No hyper parameters to optimize')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='ru_nner_config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='Runner', ctx=Load()), Name(id='con_fig', ctx=Load())], keywords=[])), Assign(targets=[Name(id='trainer_config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='Trainer', ctx=Load()), Subscript(value=Name(id='ru_nner_config', ctx=Load()), slice=Constant(value='trainer_params'), ctx=Load())], keywords=[])), Assign(targets=[Tuple(elts=[Name(id='_hopt_backend', ctx=Store()), Name(id='hopt', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Subscript(value=Name(id='ru_nner_config', ctx=Load()), slice=Constant(value='hopt_backend'), ctx=Load()), attr='split', ctx=Load()), args=[Constant(value='-')], keywords=[])), Assert(test=Compare(left=Name(id='_hopt_backend', ctx=Load()), ops=[Eq()], comparators=[Constant(value='optuna')])), Assign(targets=[Name(id='study', ctx=Store())], value=Call(func=Attribute(value=Name(id='optuna', ctx=Load()), attr='create_study', ctx=Load()), args=[], keywords=[keyword(arg='direction', value=IfExp(test=Subscript(value=Name(id='trainer_config', ctx=Load()), slice=Constant(value='selection_minimize'), ctx=Load()), body=Constant(value='minimize'), orelse=Constant(value='maximize'))), keyword(arg='sampler', value=Call(func=Subscript(value=Name(id='SAM', ctx=Load()), slice=Name(id='hopt', ctx=Load()), ctx=Load()), args=[], keywords=[]))])), Assign(targets=[Name(id='worker', ctx=Store())], value=Call(func=Name(id='HoptWorker', ctx=Load()), args=[Name(id='args', ctx=Load()), Constant(value='optuna'), Name(id='run_cvaldpDN', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='study', ctx=Load()), attr='optimize', ctx=Load()), args=[Name(id='worker', ctx=Load())], keywords=[keyword(arg='n_trials', value=Subscript(value=Name(id='ru_nner_config', ctx=Load()), slice=Constant(value='num_hopt_trials'), ctx=Load()))]))], decorator_list=[]), FunctionDef(name='hopt_wandb', args=arguments(posonlyargs=[], args=[arg(arg='args'), arg(arg='run_cvaldpDN')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=True)]), body=[Assign(targets=[Tuple(elts=[Name(id='LOGGER_TYPE', ctx=Store()), Name(id='PROJECT', ctx=Store()), Name(id='experiment', ctx=Store()), Name(id='groupUbeuj', ctx=Store())], ctx=Store())], value=Call(func=Name(id='parse_logger', ctx=Load()), args=[Attribute(value=Name(id='args', ctx=Load()), attr='logger', ctx=Load())], keywords=[])), If(test=Compare(left=Name(id='LOGGER_TYPE', ctx=Load()), ops=[NotEq()], comparators=[Constant(value='wandb')]), body=[Raise(exc=Call(func=Name(id='runtimeerror', ctx=Load()), args=[Constant(value='Need wandb logger for wandb-based hyperparameter search')], keywords=[]))], orelse=[]), If(test=Compare(left=Name(id='experiment', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='runtimeerror', ctx=Load()), args=[Constant(value='Need experiment name for hyperparameter search')], keywords=[]))], orelse=[]), If(test=Compare(left=Attribute(value=Name(id='args', ctx=Load()), attr='sweep_id', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Assign(targets=[Tuple(elts=[Name(id='swee', ctx=Store()), Name(id='count', ctx=Store())], ctx=Store())], value=Tuple(elts=[Attribute(value=Name(id='args', ctx=Load()), attr='sweep_id', ctx=Load()), Constant(value=None)], ctx=Load()))], orelse=[Assign(targets=[Tuple(elts=[Name(id='swee', ctx=Store()), Name(id='count', ctx=Store())], ctx=Store())], value=Call(func=Name(id='make_sweep', ctx=Load()), args=[Name(id='PROJECT', ctx=Load()), Name(id='experiment', ctx=Load()), Attribute(value=Name(id='args', ctx=Load()), attr='config', ctx=Load())], keywords=[]))]), Assign(targets=[Name(id='worker', ctx=Store())], value=Call(func=Name(id='HoptWorker', ctx=Load()), args=[Name(id='args', ctx=Load()), BinOp(left=Constant(value='sweep-'), op=Add(), right=Name(id='swee', ctx=Load())), Name(id='run_cvaldpDN', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='wandb', ctx=Load()), attr='agent', ctx=Load()), args=[Name(id='swee', ctx=Load())], keywords=[keyword(arg='function', value=Name(id='worker', ctx=Load())), keyword(arg='project', value=Name(id='PROJECT', ctx=Load())), keyword(arg='count', value=Name(id='count', ctx=Load()))])), Expr(value=Call(func=Name(id='prin_t', ctx=Load()), args=[Constant(value='Finished sweep'), Name(id='swee', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='suggest', args=arguments(posonlyargs=[], args=[arg(arg='trial'), arg(arg='name_'), arg(arg='spe')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' ơ˻ ȸʠɌ  ͦŇ  ͕ɲ    ')), If(test=UnaryOp(op=Not(), operand=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='spe', ctx=Load()), Tuple(elts=[Name(id='dictZ', ctx=Load()), Name(id='OrderedDict', ctx=Load())], ctx=Load())], keywords=[])), body=[Raise(exc=Call(func=Name(id='ValueErrorWT', ctx=Load()), args=[Call(func=Attribute(value=Constant(value='Dictionary HOPT specification is expected, got {} for {}.'), attr='format', ctx=Load()), args=[Name(id='spe', ctx=Load()), Name(id='name_', ctx=Load())], keywords=[])], keywords=[]))], orelse=[]), If(test=Compare(left=Constant(value='values'), ops=[In()], comparators=[Name(id='spe', ctx=Load())]), body=[Return(value=Call(func=Attribute(value=Name(id='trial', ctx=Load()), attr='suggest_categorical', ctx=Load()), args=[Name(id='name_', ctx=Load()), Subscript(value=Name(id='spe', ctx=Load()), slice=Constant(value='values'), ctx=Load())], keywords=[]))], orelse=[]), Assign(targets=[Name(id='distribution', ctx=Store())], value=Call(func=Attribute(value=Name(id='spe', ctx=Load()), attr='get', ctx=Load()), args=[Constant(value='distribution'), Constant(value='uniform')], keywords=[])), If(test=Compare(left=Name(id='distribution', ctx=Load()), ops=[Eq()], comparators=[Constant(value='log_uniform')]), body=[Return(value=Call(func=Attribute(value=Name(id='trial', ctx=Load()), attr='suggest_loguniform', ctx=Load()), args=[Name(id='name_', ctx=Load()), Call(func=Attribute(value=Name(id='math', ctx=Load()), attr='exp', ctx=Load()), args=[Subscript(value=Name(id='spe', ctx=Load()), slice=Constant(value='min'), ctx=Load())], keywords=[]), Call(func=Attribute(value=Name(id='math', ctx=Load()), attr='exp', ctx=Load()), args=[Subscript(value=Name(id='spe', ctx=Load()), slice=Constant(value='max'), ctx=Load())], keywords=[])], keywords=[]))], orelse=[]), If(test=Compare(left=Name(id='distribution', ctx=Load()), ops=[NotEq()], comparators=[Constant(value='uniform')]), body=[Raise(exc=Call(func=Name(id='ConfigError', ctx=Load()), args=[Call(func=Attribute(value=Constant(value='Unknown distribution: {}.'), attr='format', ctx=Load()), args=[Name(id='distribution', ctx=Load())], keywords=[])], keywords=[]))], orelse=[]), If(test=BoolOp(op=Or(), values=[Call(func=Name(id='isinstance', ctx=Load()), args=[Subscript(value=Name(id='spe', ctx=Load()), slice=Constant(value='min'), ctx=Load()), Name(id='float', ctx=Load())], keywords=[]), Call(func=Name(id='isinstance', ctx=Load()), args=[Subscript(value=Name(id='spe', ctx=Load()), slice=Constant(value='max'), ctx=Load()), Name(id='float', ctx=Load())], keywords=[])]), body=[Return(value=Call(func=Attribute(value=Name(id='trial', ctx=Load()), attr='suggest_uniform', ctx=Load()), args=[Name(id='name_', ctx=Load()), Subscript(value=Name(id='spe', ctx=Load()), slice=Constant(value='min'), ctx=Load()), Subscript(value=Name(id='spe', ctx=Load()), slice=Constant(value='max'), ctx=Load())], keywords=[]))], orelse=[Return(value=Call(func=Attribute(value=Name(id='trial', ctx=Load()), attr='suggest_int', ctx=Load()), args=[Name(id='name_', ctx=Load()), Subscript(value=Name(id='spe', ctx=Load()), slice=Constant(value='min'), ctx=Load()), Subscript(value=Name(id='spe', ctx=Load()), slice=Constant(value='max'), ctx=Load())], keywords=[]))])], decorator_list=[]), Assign(targets=[Name(id='BACKENDS', ctx=Store())], value=Dict(keys=[Constant(value='wandb-bayes'), Constant(value='wandb-random'), Constant(value='optuna-tpe')], values=[Name(id='hopt_wandb', ctx=Load()), Name(id='hopt_wandb', ctx=Load()), Name(id='hopt_optuna', ctx=Load())])), FunctionDef(name='hop', args=arguments(posonlyargs=[], args=[arg(arg='args'), arg(arg='run_cvaldpDN')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=True)]), body=[Expr(value=Constant(value='ƊRuǃʤɮȜn ɖhČ$Ĳopṯ tuɈƥningĕ.')), Expr(value=Call(func=Name(id='make_directory', ctx=Load()), args=[Attribute(value=Name(id='args', ctx=Load()), attr='train_root', ctx=Load())], keywords=[])), Assign(targets=[Name(id='con_fig', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='Runner', ctx=Load()), Attribute(value=Name(id='args', ctx=Load()), attr='config', ctx=Load())], keywords=[])), Assign(targets=[Name(id='con_fig', ctx=Store())], value=Call(func=Name(id='update_config', ctx=Load()), args=[Name(id='con_fig', ctx=Load()), Subscript(value=Name(id='con_fig', ctx=Load()), slice=Constant(value='hopt_params'), ctx=Load())], keywords=[])), Delete(targets=[Subscript(value=Name(id='con_fig', ctx=Load()), slice=Constant(value='seed'), ctx=Del())]), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='tempfile', ctx=Load()), attr='NamedTemporaryFile', ctx=Load()), args=[Constant(value='w')], keywords=[]), optional_vars=Name(id='fp', ctx=Store()))], body=[Expr(value=Call(func=Name(id='write_config', ctx=Load()), args=[Name(id='con_fig', ctx=Load()), Name(id='fp', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='fp', ctx=Load()), attr='flush', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='args', ctx=Store())], value=Call(func=Attribute(value=Name(id='copy', ctx=Load()), attr='deepcopy', ctx=Load()), args=[Name(id='args', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='args', ctx=Load()), attr='config', ctx=Store())], value=Attribute(value=Name(id='fp', ctx=Load()), attr='name', ctx=Load())), Expr(value=Call(func=Subscript(value=Name(id='BACKENDS', ctx=Load()), slice=Subscript(value=Name(id='con_fig', ctx=Load()), slice=Constant(value='hopt_backend'), ctx=Load()), ctx=Load()), args=[Name(id='args', ctx=Load())], keywords=[keyword(arg='run_cval', value=Name(id='run_cvaldpDN', ctx=Load()))]))])], decorator_list=[])], type_ignores=[])
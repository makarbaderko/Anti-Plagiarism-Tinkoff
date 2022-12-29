Module(body=[Import(names=[alias(name='os')]), ImportFrom(module='common', names=[alias(name='aggregate_metrics'), alias(name='log_wandb_metrics'), alias(name='make_directory'), alias(name='patch_cmd'), alias(name='print_nested')], level=1), ImportFrom(module='collections', names=[alias(name='OrderedDict')], level=0), ImportFrom(module='config', names=[alias(name='read_config'), alias(name='write_config'), alias(name='prepare_config'), alias(name='as_flat_config'), alias(name='as_nested_config')], level=2), Import(names=[alias(name='subprocess')]), ImportFrom(module='runner', names=[alias(name='Runner'), alias(name='parse_logger')], level=2), ImportFrom(module='io', names=[alias(name='read_yaml'), alias(name='write_yaml')], level=2), FunctionDef(name='get_train_root', args=arguments(posonlyargs=[], args=[arg(arg='train_r_oot'), arg(arg='seed')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None)]), body=[Assign(targets=[Name(id='parts', ctx=Store())], value=List(elts=[Name(id='train_r_oot', ctx=Load())], ctx=Load())), If(test=Compare(left=Name(id='seed', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Expr(value=Call(func=Attribute(value=Name(id='parts', ctx=Load()), attr='append', ctx=Load()), args=[Call(func=Attribute(value=Constant(value='seed-{}'), attr='format', ctx=Load()), args=[Name(id='seed', ctx=Load())], keywords=[])], keywords=[]))], orelse=[]), Assign(targets=[Name(id='pat_h', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Starred(value=Name(id='parts', ctx=Load()), ctx=Load())], keywords=[])), Expr(value=Call(func=Name(id='make_directory', ctx=Load()), args=[Name(id='pat_h', ctx=Load())], keywords=[])), Return(value=Name(id='pat_h', ctx=Load()))], decorator_list=[]), FunctionDef(name='patch_logger', args=arguments(posonlyargs=[], args=[arg(arg='logger'), arg(arg='seed')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='logger_type', ctx=Store()), Name(id='projectfQlhl', ctx=Store()), Name(id='experiment', ctx=Store()), Name(id='group', ctx=Store())], ctx=Store())], value=Call(func=Name(id='parse_logger', ctx=Load()), args=[Name(id='logger', ctx=Load())], keywords=[])), If(test=Compare(left=Name(id='logger_type', ctx=Load()), ops=[Eq()], comparators=[Constant(value='tensorboard')]), body=[Assign(targets=[Name(id='logger', ctx=Store())], value=Constant(value='tensorboard'))], orelse=[If(test=Compare(left=Name(id='logger_type', ctx=Load()), ops=[Eq()], comparators=[Constant(value='wandb')]), body=[If(test=Compare(left=Name(id='group', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Assign(targets=[Name(id='group', ctx=Store())], value=Name(id='experiment', ctx=Load()))], orelse=[]), Assign(targets=[Name(id='experiment', ctx=Store())], value=BinOp(left=Name(id='experiment', ctx=Load()), op=Add(), right=Call(func=Attribute(value=Constant(value='-seed-{}'), attr='format', ctx=Load()), args=[Name(id='seed', ctx=Load())], keywords=[]))), Assign(targets=[Name(id='logger', ctx=Store())], value=Call(func=Attribute(value=Constant(value=':'), attr='join', ctx=Load()), args=[List(elts=[Name(id='logger_type', ctx=Load()), Name(id='projectfQlhl', ctx=Load()), Name(id='experiment', ctx=Load()), Name(id='group', ctx=Load())], ctx=Load())], keywords=[]))], orelse=[])]), Return(value=Name(id='logger', ctx=Load()))], decorator_list=[]), FunctionDef(name='get_train_cmdPX', args=arguments(posonlyargs=[], args=[arg(arg='arg_s'), arg(arg='seed'), arg(arg='run_cval')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=True)]), body=[Assign(targets=[Name(id='top_ro', ctx=Store())], value=Attribute(value=Name(id='arg_s', ctx=Load()), attr='train_root', ctx=Load())), Assign(targets=[Name(id='train_r_oot', ctx=Store())], value=Call(func=Name(id='get_train_root', ctx=Load()), args=[Name(id='top_ro', ctx=Load()), Name(id='seed', ctx=Load())], keywords=[])), Assign(targets=[Name(id='config', ctx=Store())], value=IfExp(test=Compare(left=Attribute(value=Name(id='arg_s', ctx=Load()), attr='config', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=Call(func=Name(id='read_config', ctx=Load()), args=[Attribute(value=Name(id='arg_s', ctx=Load()), attr='config', ctx=Load())], keywords=[]), orelse=Dict(keys=[], values=[]))), Assign(targets=[Subscript(value=Name(id='config', ctx=Load()), slice=Constant(value='seed'), ctx=Store())], value=Name(id='seed', ctx=Load())), Assign(targets=[Name(id='config_p', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='train_r_oot', ctx=Load()), Constant(value='config.yaml')], keywords=[])), Expr(value=Call(func=Name(id='write_config', ctx=Load()), args=[Name(id='config', ctx=Load()), Name(id='config_p', ctx=Load())], keywords=[])), Assign(targets=[Name(id='new_arg', ctx=Store())], value=Dict(keys=[Constant(value='--config'), Constant(value='--train-root'), Constant(value='--logger')], values=[Name(id='config_p', ctx=Load()), Name(id='train_r_oot', ctx=Load()), Call(func=Name(id='patch_logger', ctx=Load()), args=[Attribute(value=Name(id='arg_s', ctx=Load()), attr='logger', ctx=Load()), Subscript(value=Name(id='config', ctx=Load()), slice=Constant(value='seed'), ctx=Load())], keywords=[])])), If(test=Compare(left=Attribute(value=Name(id='arg_s', ctx=Load()), attr='checkpoint', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Assign(targets=[Subscript(value=Name(id='new_arg', ctx=Load()), slice=Constant(value='--checkpoint'), ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='arg_s', ctx=Load()), attr='checkpoint', ctx=Load()), attr='replace', ctx=Load()), args=[Constant(value='{seed}'), Call(func=Name(id='str', ctx=Load()), args=[Name(id='seed', ctx=Load())], keywords=[])], keywords=[]))], orelse=[]), Assign(targets=[Name(id='cmd', ctx=Store())], value=IfExp(test=Name(id='run_cval', ctx=Load()), body=Constant(value='cval'), orelse=Constant(value='train'))), Return(value=Tuple(elts=[Attribute(value=Name(id='os', ctx=Load()), attr='environ', ctx=Load()), Call(func=Name(id='patch_cmd', ctx=Load()), args=[Name(id='cmd', ctx=Load()), Name(id='new_arg', ctx=Load())], keywords=[])], ctx=Load()))], decorator_list=[]), FunctionDef(name='read_metrics_no_std', args=arguments(posonlyargs=[], args=[arg(arg='pat_h')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='metr', ctx=Store())], value=Call(func=Name(id='read_yaml', ctx=Load()), args=[Name(id='pat_h', ctx=Load())], keywords=[])), Assign(targets=[Name(id='fl', ctx=Store())], value=Call(func=Name(id='as_flat_config', ctx=Load()), args=[Name(id='metr', ctx=Load())], keywords=[])), Assign(targets=[Name(id='flat__no_std', ctx=Store())], value=Call(func=Name(id='OrderedDict', ctx=Load()), args=[ListComp(elt=Tuple(elts=[Name(id='k', ctx=Load()), Name(id='V', ctx=Load())], ctx=Load()), generators=[comprehension(target=Tuple(elts=[Name(id='k', ctx=Store()), Name(id='V', ctx=Store())], ctx=Store()), iter=Call(func=Attribute(value=Name(id='fl', ctx=Load()), attr='items', ctx=Load()), args=[], keywords=[]), ifs=[Compare(left=Constant(value='_std'), ops=[NotIn()], comparators=[Name(id='k', ctx=Load())])], is_async=0)])], keywords=[])), Assign(targets=[Name(id='metrics_no_std', ctx=Store())], value=Call(func=Name(id='as_nested_config', ctx=Load()), args=[Name(id='flat__no_std', ctx=Load())], keywords=[])), Return(value=Name(id='metrics_no_std', ctx=Load()))], decorator_list=[]), FunctionDef(name='evaluate', args=arguments(posonlyargs=[], args=[arg(arg='arg_s'), arg(arg='run_cval')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=True)]), body=[Assign(targets=[Name(id='config', ctx=Store())], value=IfExp(test=Compare(left=Attribute(value=Name(id='arg_s', ctx=Load()), attr='config', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=Call(func=Name(id='read_config', ctx=Load()), args=[Attribute(value=Name(id='arg_s', ctx=Load()), attr='config', ctx=Load())], keywords=[]), orelse=Dict(keys=[], values=[]))), Assign(targets=[Name(id='config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Call(func=Attribute(value=Name(id='Runner', ctx=Load()), attr='get_default_config', ctx=Load()), args=[], keywords=[]), Name(id='config', ctx=Load())], keywords=[])), Assign(targets=[Name(id='num_seeds', ctx=Store())], value=Subscript(value=Name(id='config', ctx=Load()), slice=Constant(value='num_evaluation_seeds'), ctx=Load())), Expr(value=Call(func=Name(id='make_directory', ctx=Load()), args=[Attribute(value=Name(id='arg_s', ctx=Load()), attr='train_root', ctx=Load())], keywords=[])), For(target=Name(id='seed', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Attribute(value=Name(id='arg_s', ctx=Load()), attr='from_seed', ctx=Load()), Name(id='num_seeds', ctx=Load())], keywords=[]), body=[Assign(targets=[Tuple(elts=[Name(id='env', ctx=Store()), Name(id='cmd', ctx=Store())], ctx=Store())], value=Call(func=Name(id='get_train_cmdPX', ctx=Load()), args=[Name(id='arg_s', ctx=Load()), Name(id='seed', ctx=Load())], keywords=[keyword(arg='run_cval', value=Name(id='run_cval', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='subprocess', ctx=Load()), attr='call', ctx=Load()), args=[Name(id='cmd', ctx=Load())], keywords=[keyword(arg='env', value=Name(id='env', ctx=Load())), keyword(arg='cwd', value=Call(func=Attribute(value=Name(id='os', ctx=Load()), attr='getcwd', ctx=Load()), args=[], keywords=[]))]))], orelse=[]), Assign(targets=[Name(id='metr', ctx=Store())], value=Call(func=Name(id='aggregate_metrics', ctx=Load()), args=[Starred(value=ListComp(elt=Call(func=Name(id='read_metrics_no_std', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Call(func=Name(id='get_train_root', ctx=Load()), args=[Attribute(value=Name(id='arg_s', ctx=Load()), attr='train_root', ctx=Load()), Name(id='seed', ctx=Load())], keywords=[]), Constant(value='metrics.yaml')], keywords=[])], keywords=[]), generators=[comprehension(target=Name(id='seed', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Name(id='num_seeds', ctx=Load())], keywords=[]), ifs=[], is_async=0)]), ctx=Load())], keywords=[])), Expr(value=Call(func=Name(id='log_wandb_metrics', ctx=Load()), args=[Name(id='metr', ctx=Load()), Attribute(value=Name(id='arg_s', ctx=Load()), attr='logger', ctx=Load())], keywords=[])), Assign(targets=[Subscript(value=Name(id='metr', ctx=Load()), slice=Constant(value='num_seeds'), ctx=Store())], value=Name(id='num_seeds', ctx=Load())), Expr(value=Call(func=Name(id='print_nested', ctx=Load()), args=[Name(id='metr', ctx=Load())], keywords=[])), Expr(value=Call(func=Name(id='write_yaml', ctx=Load()), args=[Name(id='metr', ctx=Load()), Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Attribute(value=Name(id='arg_s', ctx=Load()), attr='train_root', ctx=Load()), Constant(value='metrics.yaml')], keywords=[])], keywords=[]))], decorator_list=[])], type_ignores=[])
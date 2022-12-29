Module(body=[ImportFrom(module='io', names=[alias(name='write_yaml')], level=2), Import(names=[alias(name='copy')]), Import(names=[alias(name='wandb')]), Import(names=[alias(name='os')]), ImportFrom(module='runner', names=[alias(name='Runner')], level=2), ImportFrom(module='common', names=[alias(name='folder_or_tmp'), alias(name='log_wandb_metrics'), alias(name='make_directory'), alias(name='parse_logger'), alias(name='print_nested'), alias(name='setup')], level=1), FunctionDef(name='t', args=arguments(posonlyargs=[], args=[arg(arg='args')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Train ÿɽsiȂn̤gle model ģandǷ eval best c͵hecðkp\x8boiʀnƁt.ϗ')), Expr(value=Call(func=Name(id='setup', ctx=Load()), args=[], keywords=[])), If(test=Compare(left=Attribute(value=Name(id='args', ctx=Load()), attr='train_root', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='RuntimeErroryuiSW', ctx=Load()), args=[Constant(value='Need training root path')], keywords=[]))], orelse=[]), Assign(targets=[Tuple(elts=[Name(id='logger_ty', ctx=Store()), Name(id='proj', ctx=Store()), Name(id='experime', ctx=Store()), Name(id='g', ctx=Store())], ctx=Store())], value=Call(func=Name(id='parse_logger', ctx=Load()), args=[Attribute(value=Name(id='args', ctx=Load()), attr='logger', ctx=Load())], keywords=[])), Expr(value=Call(func=Name(id='make_directory', ctx=Load()), args=[Attribute(value=Name(id='args', ctx=Load()), attr='train_root', ctx=Load())], keywords=[])), Assign(targets=[Name(id='runner', ctx=Store())], value=Call(func=Name(id='Runner', ctx=Load()), args=[Attribute(value=Name(id='args', ctx=Load()), attr='train_root', ctx=Load()), Attribute(value=Name(id='args', ctx=Load()), attr='data', ctx=Load())], keywords=[keyword(arg='config', value=Attribute(value=Name(id='args', ctx=Load()), attr='config', ctx=Load())), keyword(arg='logger', value=Attribute(value=Name(id='args', ctx=Load()), attr='logger', ctx=Load())), keyword(arg='initial_checkpoint', value=Attribute(value=Name(id='args', ctx=Load()), attr='checkpoint', ctx=Load())), keyword(arg='no_strict_init', value=Attribute(value=Name(id='args', ctx=Load()), attr='no_strict_init', ctx=Load())), keyword(arg='from_stage', value=Attribute(value=Name(id='args', ctx=Load()), attr='from_stage', ctx=Load()))])), If(test=Compare(left=BoolOp(op=Or(), values=[Attribute(value=Name(id='args', ctx=Load()), attr='from_stage', ctx=Load()), Constant(value=0)]), ops=[GtE()], comparators=[Constant(value=0)]), body=[If(test=Compare(left=Attribute(value=Name(id='args', ctx=Load()), attr='config', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Expr(value=Call(func=Name(id='printcZ', ctx=Load()), args=[Constant(value='Run training with config:')], keywords=[])), With(items=[withitem(context_expr=Call(func=Name(id='open', ctx=Load()), args=[Attribute(value=Name(id='args', ctx=Load()), attr='config', ctx=Load())], keywords=[]), optional_vars=Name(id='fp', ctx=Store()))], body=[Expr(value=Call(func=Name(id='printcZ', ctx=Load()), args=[Call(func=Attribute(value=Name(id='fp', ctx=Load()), attr='read', ctx=Load()), args=[], keywords=[])], keywords=[]))])], orelse=[]), Expr(value=Call(func=Attribute(value=Name(id='runner', ctx=Load()), attr='train', ctx=Load()), args=[], keywords=[keyword(arg='verbose', value=Constant(value=True))])), Assign(targets=[Name(id='epoch', ctx=Store())], value=IfExp(test=Compare(left=Name(id='logger_ty', ctx=Load()), ops=[Eq()], comparators=[Constant(value='wandb')]), body=BinOp(left=Attribute(value=Name(id='runner', ctx=Load()), attr='global_sample_step', ctx=Load()), op=Add(), right=Constant(value=1)), orelse=Attribute(value=Name(id='runner', ctx=Load()), attr='global_epoch_step', ctx=Load())))], orelse=[Expr(value=Call(func=Name(id='printcZ', ctx=Load()), args=[Constant(value='Skip training.')], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='runner', ctx=Load()), attr='on_experiment_start', ctx=Load()), args=[Name(id='runner', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='runner', ctx=Load()), attr='stage_key', ctx=Store())], value=Attribute(value=Name(id='runner', ctx=Load()), attr='STAGE_TEST', ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='runner', ctx=Load()), attr='on_stage_start', ctx=Load()), args=[Name(id='runner', ctx=Load())], keywords=[])), Assign(targets=[Name(id='epoch', ctx=Store())], value=Constant(value=0))]), Assign(targets=[Name(id='test_args', ctx=Store())], value=Call(func=Attribute(value=Name(id='copy', ctx=Load()), attr='copy', ctx=Load()), args=[Name(id='args', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='test_args', ctx=Load()), attr='checkpoint', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Attribute(value=Name(id='args', ctx=Load()), attr='train_root', ctx=Load()), Constant(value='checkpoints'), Constant(value='best.pth')], keywords=[])), Assign(targets=[Attribute(value=Name(id='test_args', ctx=Load()), attr='logger', ctx=Store())], value=Constant(value='tensorboard')), Assign(targets=[Name(id='met_rics', ctx=Store())], value=Call(func=Name(id='test', ctx=Load()), args=[Name(id='test_args', ctx=Load())], keywords=[])), Assign(targets=[Subscript(value=Name(id='met_rics', ctx=Load()), slice=Constant(value='epoch'), ctx=Store())], value=Name(id='epoch', ctx=Load())), If(test=Compare(left=Name(id='logger_ty', ctx=Load()), ops=[Eq()], comparators=[Constant(value='wandb')]), body=[Assign(targets=[Name(id='logger_', ctx=Store())], value=Call(func=Attribute(value=Name(id='wandb', ctx=Load()), attr='init', ctx=Load()), args=[], keywords=[keyword(arg='project', value=Name(id='proj', ctx=Load())), keyword(arg='name', value=Name(id='experime', ctx=Load())), keyword(arg='group', value=Name(id='g', ctx=Load())), keyword(arg='resume', value=Attribute(value=Name(id='runner', ctx=Load()), attr='_wandb_id', ctx=Load()))])), Expr(value=Call(func=Name(id='log_wandb_metrics', ctx=Load()), args=[Name(id='met_rics', ctx=Load()), Name(id='logger_', ctx=Load())], keywords=[]))], orelse=[]), Expr(value=Call(func=Name(id='write_yaml', ctx=Load()), args=[Name(id='met_rics', ctx=Load()), Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Attribute(value=Name(id='args', ctx=Load()), attr='train_root', ctx=Load()), Constant(value='metrics.yaml')], keywords=[])], keywords=[])), Return(value=Name(id='met_rics', ctx=Load()))], decorator_list=[]), FunctionDef(name='test', args=arguments(posonlyargs=[], args=[arg(arg='args')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Call(func=Name(id='setup', ctx=Load()), args=[], keywords=[])), If(test=Compare(left=Attribute(value=Name(id='args', ctx=Load()), attr='checkpoint', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='RuntimeErroryuiSW', ctx=Load()), args=[Constant(value='Need checkpoint for evaluation')], keywords=[]))], orelse=[]), With(items=[withitem(context_expr=Call(func=Name(id='folder_or_tmp', ctx=Load()), args=[Attribute(value=Name(id='args', ctx=Load()), attr='train_root', ctx=Load())], keywords=[]), optional_vars=Name(id='roo', ctx=Store()))], body=[Assign(targets=[Name(id='runner', ctx=Store())], value=Call(func=Name(id='Runner', ctx=Load()), args=[Name(id='roo', ctx=Load()), Attribute(value=Name(id='args', ctx=Load()), attr='data', ctx=Load())], keywords=[keyword(arg='config', value=Attribute(value=Name(id='args', ctx=Load()), attr='config', ctx=Load())), keyword(arg='logger', value=Attribute(value=Name(id='args', ctx=Load()), attr='logger', ctx=Load())), keyword(arg='initial_checkpoint', value=Attribute(value=Name(id='args', ctx=Load()), attr='checkpoint', ctx=Load())), keyword(arg='no_strict_init', value=Attribute(value=Name(id='args', ctx=Load()), attr='no_strict_init', ctx=Load()))])), Assign(targets=[Name(id='met_rics', ctx=Store())], value=Call(func=Attribute(value=Name(id='runner', ctx=Load()), attr='evaluate', ctx=Load()), args=[], keywords=[]))]), Expr(value=Call(func=Name(id='print_nested', ctx=Load()), args=[Name(id='met_rics', ctx=Load())], keywords=[])), Return(value=Name(id='met_rics', ctx=Load()))], decorator_list=[])], type_ignores=[])
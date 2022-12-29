Module(body=[ImportFrom(module='collections', names=[alias(name='OrderedDict')], level=0), Import(names=[alias(name='torch')]), ImportFrom(module='config', names=[alias(name='prepare_config')], level=2), ClassDef(name='StepScheduler', bases=[Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='optim', ctx=Load()), attr='lr_scheduler', ctx=Load()), attr='StepLR', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Cːonƕfig͎͎RΞurǞϗ̵abηleΦƦ LR s͢ɚcȸϡhedƵul¹erȸ.')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='optimizer'), arg(arg='num_epochs')], kwonlyargs=[arg(arg='minimize_metric'), arg(arg='config')], kw_defaults=[Constant(value=True), Constant(value=None)], defaults=[]), body=[Assign(targets=[Name(id='config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='self', ctx=Load()), Name(id='config', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[Name(id='optimizer', ctx=Load())], keywords=[keyword(arg='step_size', value=Subscript(value=Name(id='config', ctx=Load()), slice=Constant(value='step'), ctx=Load())), keyword(arg='gamma', value=Subscript(value=Name(id='config', ctx=Load()), slice=Constant(value='gamma'), ctx=Load()))]))], decorator_list=[]), FunctionDef(name='get_default_conf_ig', args=arguments(posonlyargs=[], args=[arg(arg='step'), arg(arg='gamma')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=10), Constant(value=0.1)]), body=[Expr(value=Constant(value='GĚƊǹet s\x88cheduleÏr paraȅmetʪe\u0380rs.')), Return(value=Call(func=Name(id='OrderedDict', ctx=Load()), args=[List(elts=[Tuple(elts=[Constant(value='step'), Name(id='step', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='gamma'), Name(id='gamma', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[]))], decorator_list=[Name(id='staticmethod', ctx=Load())])], decorator_list=[]), ClassDef(name='MultiStepScheduler', bases=[Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='optim', ctx=Load()), attr='lr_scheduler', ctx=Load()), attr='MultiStepLR', ctx=Load())], keywords=[], body=[FunctionDef(name='get_default_conf_ig', args=arguments(posonlyargs=[], args=[arg(arg='milestones'), arg(arg='gamma')], kwonlyargs=[], kw_defaults=[], defaults=[List(elts=[Constant(value=9), Constant(value=14)], ctx=Load()), Constant(value=0.1)]), body=[Expr(value=Constant(value='ɔGeřƾȉt Ǽsΐchte\x98d˞uƝl;er pǡƂƓaκrĢamet-ers¬ιȂ.')), Return(value=Call(func=Name(id='OrderedDict', ctx=Load()), args=[List(elts=[Tuple(elts=[Constant(value='milestones'), Name(id='milestones', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='gamma'), Name(id='gamma', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[]))], decorator_list=[Name(id='staticmethod', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='optimizer'), arg(arg='num_epochs')], kwonlyargs=[arg(arg='minimize_metric'), arg(arg='config')], kw_defaults=[Constant(value=True), Constant(value=None)], defaults=[]), body=[Assign(targets=[Name(id='config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='self', ctx=Load()), Name(id='config', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[Name(id='optimizer', ctx=Load())], keywords=[keyword(arg='milestones', value=Subscript(value=Name(id='config', ctx=Load()), slice=Constant(value='milestones'), ctx=Load())), keyword(arg='gamma', value=Subscript(value=Name(id='config', ctx=Load()), slice=Constant(value='gamma'), ctx=Load()))]))], decorator_list=[])], decorator_list=[]), ClassDef(name='PlateauSchedulerDfsg', bases=[Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='optim', ctx=Load()), attr='lr_scheduler', ctx=Load()), attr='ReduceLROnPlateau', ctx=Load())], keywords=[], body=[FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='optimizer'), arg(arg='num_epochs')], kwonlyargs=[arg(arg='minimize_metric'), arg(arg='config')], kw_defaults=[Constant(value=True), Constant(value=None)], defaults=[]), body=[Expr(value=Constant(value=' tT ɓ  ')), Assign(targets=[Name(id='config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='self', ctx=Load()), Name(id='config', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[Name(id='optimizer', ctx=Load())], keywords=[keyword(arg='mode', value=IfExp(test=Name(id='minimize_metric', ctx=Load()), body=Constant(value='min'), orelse=Constant(value='max'))), keyword(arg='patience', value=Subscript(value=Name(id='config', ctx=Load()), slice=Constant(value='patience'), ctx=Load())), keyword(arg='factor', value=Subscript(value=Name(id='config', ctx=Load()), slice=Constant(value='factor'), ctx=Load()))]))], decorator_list=[]), FunctionDef(name='get_default_conf_ig', args=arguments(posonlyargs=[], args=[arg(arg='patience'), arg(arg='factor')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=10), Constant(value=0.1)]), body=[Return(value=Call(func=Name(id='OrderedDict', ctx=Load()), args=[List(elts=[Tuple(elts=[Constant(value='patience'), Name(id='patience', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='factor'), Name(id='factor', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[]))], decorator_list=[Name(id='staticmethod', ctx=Load())])], decorator_list=[]), ClassDef(name='E', bases=[Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='optim', ctx=Load()), attr='lr_scheduler', ctx=Load()), attr='ExponentialLR', ctx=Load())], keywords=[], body=[FunctionDef(name='get_default_conf_ig', args=arguments(posonlyargs=[], args=[arg(arg='lr_at_last_epoch')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=0.0001)]), body=[Expr(value=Constant(value='DGet schedȬuler parǴameters.')), Return(value=Call(func=Name(id='OrderedDict', ctx=Load()), args=[List(elts=[Tuple(elts=[Constant(value='lr_at_last_epoch'), Name(id='lr_at_last_epoch', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[]))], decorator_list=[Name(id='staticmethod', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='optimizer'), arg(arg='num_epochs')], kwonlyargs=[arg(arg='minimize_metric'), arg(arg='config')], kw_defaults=[Constant(value=True), Constant(value=None)], defaults=[]), body=[Expr(value=Constant(value=' ')), Assign(targets=[Name(id='config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='self', ctx=Load()), Name(id='config', ctx=Load())], keywords=[])), Assign(targets=[Name(id='lr_0', ctx=Store())], value=Subscript(value=Subscript(value=Attribute(value=Name(id='optimizer', ctx=Load()), attr='param_groups', ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value='lr'), ctx=Load())), Assign(targets=[Name(id='lr_t', ctx=Store())], value=Subscript(value=Name(id='config', ctx=Load()), slice=Constant(value='lr_at_last_epoch'), ctx=Load())), Assign(targets=[Name(id='t', ctx=Store())], value=Name(id='num_epochs', ctx=Load())), Assign(targets=[Name(id='gamma', ctx=Store())], value=BinOp(left=BinOp(left=Name(id='lr_t', ctx=Load()), op=Div(), right=Name(id='lr_0', ctx=Load())), op=Pow(), right=BinOp(left=Constant(value=1), op=Div(), right=Name(id='t', ctx=Load())))), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[Name(id='optimizer', ctx=Load())], keywords=[keyword(arg='gamma', value=Name(id='gamma', ctx=Load()))]))], decorator_list=[])], decorator_list=[]), ClassDef(name='WarmupScheduler', bases=[Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='optim', ctx=Load()), attr='lr_scheduler', ctx=Load()), attr='_LRScheduler', ctx=Load())], keywords=[], body=[FunctionDef(name='step', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='last_epoch', ctx=Load()), ops=[Gt()], comparators=[Constant(value=0)]), body=[Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_scheduler', ctx=Load()), attr='step', ctx=Load()), args=[], keywords=[]))], orelse=[]), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='step', ctx=Load()), args=[], keywords=[]))], decorator_list=[]), FunctionDef(name='get_lr', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Ű ')), Assign(targets=[Name(id='lr', ctx=Store())], value=IfExp(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_scheduler', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_scheduler', ctx=Load()), attr='get_last_lr', ctx=Load()), args=[], keywords=[]), orelse=Attribute(value=Name(id='self', ctx=Load()), attr='base_lrs', ctx=Load()))), If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='last_epoch', ctx=Load()), ops=[LtE()], comparators=[Attribute(value=Name(id='self', ctx=Load()), attr='_warmup_epochs', ctx=Load())]), body=[Assign(targets=[Name(id='lr', ctx=Store())], value=BinOp(left=List(elts=[Constant(value=0.0)], ctx=Load()), op=Mult(), right=Call(func=Name(id='len', ctx=Load()), args=[Name(id='lr', ctx=Load())], keywords=[])))], orelse=[If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='last_epoch', ctx=Load()), ops=[Eq()], comparators=[BinOp(left=Attribute(value=Name(id='self', ctx=Load()), attr='_warmup_epochs', ctx=Load()), op=Add(), right=Constant(value=1))]), body=[Assign(targets=[Name(id='lr', ctx=Store())], value=Attribute(value=Name(id='self', ctx=Load()), attr='base_lrs', ctx=Load()))], orelse=[])]), Return(value=Name(id='lr', ctx=Load()))], decorator_list=[]), FunctionDef(name='load_state_dict', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='state_dict')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='state_dict', ctx=Store())], value=Call(func=Attribute(value=Name(id='state_dict', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_warmup_epochs', ctx=Store())], value=Call(func=Attribute(value=Name(id='state_dict', ctx=Load()), attr='pop', ctx=Load()), args=[Constant(value='warmup_epochs')], keywords=[])), If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_scheduler', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_scheduler', ctx=Load()), attr='load_state_dict', ctx=Load()), args=[Name(id='state_dict', ctx=Load())], keywords=[]))], orelse=[]), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='load_state_dict', ctx=Load()), args=[Name(id='state_dict', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='state_dict', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ò ͟ ˸   Ɋ ͽ   «®  ɉ ǹ υ ʓǩ˴   Ϥ')), Assign(targets=[Name(id='st', ctx=Store())], value=IfExp(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='_scheduler', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_scheduler', ctx=Load()), attr='state_dict', ctx=Load()), args=[], keywords=[]), orelse=Dict(keys=[], values=[]))), Assign(targets=[Subscript(value=Name(id='st', ctx=Load()), slice=Constant(value='warmup_epochs'), ctx=Store())], value=Attribute(value=Name(id='self', ctx=Load()), attr='_warmup_epochs', ctx=Load())), Return(value=Name(id='st', ctx=Load()))], decorator_list=[]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='scheduler'), arg(arg='warmup_epochs')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=1)]), body=[Expr(value=Constant(value='   țK  ƚ Ź \x99ů  ü  ͙ δ Ϟ  ɡ× ΐɶ Ĳ ̍')), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_scheduler', ctx=Store())], value=Name(id='scheduler', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_warmup_epochs', ctx=Store())], value=Name(id='warmup_epochs', ctx=Load())), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='optimizer', value=Attribute(value=Name(id='scheduler', ctx=Load()), attr='optimizer', ctx=Load())), keyword(arg='last_epoch', value=Attribute(value=Name(id='scheduler', ctx=Load()), attr='last_epoch', ctx=Load())), keyword(arg='verbose', value=Attribute(value=Name(id='scheduler', ctx=Load()), attr='verbose', ctx=Load()))]))], decorator_list=[])], decorator_list=[])], type_ignores=[])
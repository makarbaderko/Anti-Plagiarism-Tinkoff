Module(body=[ImportFrom(module='collections', names=[alias(name='OrderedDict')], level=0), Import(names=[alias(name='torch')]), ImportFrom(module='config', names=[alias(name='prepare_config')], level=2), ImportFrom(module='third_party', names=[alias(name='SAM', asname='SAMImpl')], level=2), ClassDef(name='SGDOptimizer', bases=[Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='optim', ctx=Load()), attr='SGD', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Configurable SGD.')), FunctionDef(name='get_default_config', args=arguments(posonlyargs=[], args=[arg(arg='lr'), arg(arg='momentum'), arg(arg='weight_decay')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=0.1), Constant(value=0.9), Constant(value=0.0005)]), body=[Expr(value=Constant(value='Get optimizer parameters.')), Return(value=Call(func=Name(id='OrderedDict', ctx=Load()), args=[List(elts=[Tuple(elts=[Constant(value='lr'), Name(id='lr', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='momentum'), Name(id='momentum', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='weight_decay'), Name(id='weight_decay', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[]))], decorator_list=[Name(id='staticmethod', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='parameters')], kwonlyargs=[arg(arg='config')], kw_defaults=[Constant(value=None)], defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='self', ctx=Load()), Name(id='config', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[Name(id='parameters', ctx=Load())], keywords=[keyword(arg='lr', value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='lr'), ctx=Load())), keyword(arg='momentum', value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='momentum'), ctx=Load())), keyword(arg='weight_decay', value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='weight_decay'), ctx=Load()))]))], decorator_list=[]), FunctionDef(name='step', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='closure')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None)]), body=[Return(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='step', ctx=Load()), args=[], keywords=[]))], decorator_list=[Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='no_grad', ctx=Load()), args=[], keywords=[])])], decorator_list=[]), ClassDef(name='RMSpropOptimizer', bases=[Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='optim', ctx=Load()), attr='RMSprop', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Configurable RMSprop.')), FunctionDef(name='get_default_config', args=arguments(posonlyargs=[], args=[arg(arg='lr'), arg(arg='momentum'), arg(arg='weight_decay')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=0.1), Constant(value=0.9), Constant(value=0.0005)]), body=[Expr(value=Constant(value='Get optimizer parameters.')), Return(value=Call(func=Name(id='OrderedDict', ctx=Load()), args=[List(elts=[Tuple(elts=[Constant(value='lr'), Name(id='lr', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='momentum'), Name(id='momentum', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='weight_decay'), Name(id='weight_decay', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[]))], decorator_list=[Name(id='staticmethod', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='parameters')], kwonlyargs=[arg(arg='config')], kw_defaults=[Constant(value=None)], defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='self', ctx=Load()), Name(id='config', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[Name(id='parameters', ctx=Load())], keywords=[keyword(arg='lr', value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='lr'), ctx=Load())), keyword(arg='momentum', value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='momentum'), ctx=Load())), keyword(arg='weight_decay', value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='weight_decay'), ctx=Load()))]))], decorator_list=[]), FunctionDef(name='step', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='closure')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None)]), body=[Return(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='step', ctx=Load()), args=[], keywords=[]))], decorator_list=[Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='no_grad', ctx=Load()), args=[], keywords=[])])], decorator_list=[]), ClassDef(name='AdamOptimizer', bases=[Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='optim', ctx=Load()), attr='Adam', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Configurable Adam.')), FunctionDef(name='get_default_config', args=arguments(posonlyargs=[], args=[arg(arg='lr'), arg(arg='weight_decay')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=0.1), Constant(value=0.0005)]), body=[Expr(value=Constant(value='Get optimizer parameters.')), Return(value=Call(func=Name(id='OrderedDict', ctx=Load()), args=[List(elts=[Tuple(elts=[Constant(value='lr'), Name(id='lr', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='weight_decay'), Name(id='weight_decay', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[]))], decorator_list=[Name(id='staticmethod', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='parameters')], kwonlyargs=[arg(arg='config')], kw_defaults=[Constant(value=None)], defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='self', ctx=Load()), Name(id='config', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[Name(id='parameters', ctx=Load())], keywords=[keyword(arg='lr', value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='lr'), ctx=Load())), keyword(arg='weight_decay', value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='weight_decay'), ctx=Load()))]))], decorator_list=[]), FunctionDef(name='step', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='closure')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None)]), body=[Return(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='step', ctx=Load()), args=[], keywords=[]))], decorator_list=[Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='no_grad', ctx=Load()), args=[], keywords=[])])], decorator_list=[]), ClassDef(name='AdamWOptimizer', bases=[Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='optim', ctx=Load()), attr='AdamW', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Configurable AdamW.')), FunctionDef(name='get_default_config', args=arguments(posonlyargs=[], args=[arg(arg='lr'), arg(arg='weight_decay')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=0.1), Constant(value=0.0005)]), body=[Expr(value=Constant(value='Get optimizer parameters.')), Return(value=Call(func=Name(id='OrderedDict', ctx=Load()), args=[List(elts=[Tuple(elts=[Constant(value='lr'), Name(id='lr', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='weight_decay'), Name(id='weight_decay', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[]))], decorator_list=[Name(id='staticmethod', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='parameters')], kwonlyargs=[arg(arg='config')], kw_defaults=[Constant(value=None)], defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='self', ctx=Load()), Name(id='config', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[Name(id='parameters', ctx=Load())], keywords=[keyword(arg='lr', value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='lr'), ctx=Load())), keyword(arg='weight_decay', value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='weight_decay'), ctx=Load()))]))], decorator_list=[]), FunctionDef(name='step', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='closure')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None)]), body=[Return(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='step', ctx=Load()), args=[], keywords=[]))], decorator_list=[Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='no_grad', ctx=Load()), args=[], keywords=[])])], decorator_list=[]), ClassDef(name='SamOptimizer', bases=[Name(id='SAMImpl', ctx=Load())], keywords=[], body=[Assign(targets=[Name(id='BASE_OPTIMIZERS', ctx=Store())], value=Dict(keys=[Constant(value='sgd'), Constant(value='rmsprop'), Constant(value='adam'), Constant(value='adamw')], values=[Name(id='SGDOptimizer', ctx=Load()), Name(id='RMSpropOptimizer', ctx=Load()), Name(id='AdamOptimizer', ctx=Load()), Name(id='AdamWOptimizer', ctx=Load())])), FunctionDef(name='get_default_config', args=arguments(posonlyargs=[], args=[arg(arg='rho'), arg(arg='adaptive'), arg(arg='base_type'), arg(arg='base_params'), arg(arg='adaptive_bias_and_bn')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=0.5), Constant(value=True), Constant(value='sgd'), Constant(value=None), Constant(value=False)]), body=[Expr(value=Constant(value='Get optimizer parameters.')), Return(value=Call(func=Name(id='OrderedDict', ctx=Load()), args=[List(elts=[Tuple(elts=[Constant(value='rho'), Name(id='rho', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='adaptive'), Name(id='adaptive', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='base_type'), Name(id='base_type', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='base_params'), Name(id='base_params', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='adaptive_bias_and_bn'), Name(id='adaptive_bias_and_bn', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[]))], decorator_list=[Name(id='staticmethod', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='parameters')], kwonlyargs=[arg(arg='config')], kw_defaults=[Constant(value=None)], defaults=[]), body=[Assign(targets=[Name(id='config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='self', ctx=Load()), Name(id='config', ctx=Load())], keywords=[])), If(test=UnaryOp(op=Not(), operand=Subscript(value=Name(id='config', ctx=Load()), slice=Constant(value='adaptive_bias_and_bn'), ctx=Load())), body=[Assign(targets=[Name(id='parameters', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_split_bias_and_bn_groups', ctx=Load()), args=[Name(id='parameters', ctx=Load()), Dict(keys=[Constant(value='adaptive')], values=[Constant(value=False)])], keywords=[]))], orelse=[]), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[Name(id='parameters', ctx=Load()), Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='BASE_OPTIMIZERS', ctx=Load()), slice=Subscript(value=Name(id='config', ctx=Load()), slice=Constant(value='base_type'), ctx=Load()), ctx=Load())], keywords=[keyword(arg='config', value=Subscript(value=Name(id='config', ctx=Load()), slice=Constant(value='base_params'), ctx=Load())), keyword(arg='rho', value=Subscript(value=Name(id='config', ctx=Load()), slice=Constant(value='rho'), ctx=Load())), keyword(arg='adaptive', value=Subscript(value=Name(id='config', ctx=Load()), slice=Constant(value='adaptive'), ctx=Load()))]))], decorator_list=[]), FunctionDef(name='_split_bias_and_bn_groups', args=arguments(posonlyargs=[], args=[arg(arg='parameters'), arg(arg='bias_and_bn_params')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Split each parameter groups into two parts with tensors of rank > 1 and tensors of rank <= 1.\n        Apply extra parameters for those tensors with rank <= 1.')), Assign(targets=[Name(id='parameters', ctx=Store())], value=Call(func=Name(id='list', ctx=Load()), args=[Name(id='parameters', ctx=Load())], keywords=[])), If(test=UnaryOp(op=Not(), operand=Call(func=Name(id='isinstance', ctx=Load()), args=[Subscript(value=Name(id='parameters', ctx=Load()), slice=Constant(value=0), ctx=Load()), Name(id='dict', ctx=Load())], keywords=[])), body=[Assign(targets=[Name(id='parameters', ctx=Store())], value=List(elts=[Dict(keys=[Constant(value='params')], values=[Name(id='parameters', ctx=Load())])], ctx=Load()))], orelse=[]), Assign(targets=[Name(id='new_parameters', ctx=Store())], value=List(elts=[], ctx=Load())), For(target=Name(id='group', ctx=Store()), iter=Name(id='parameters', ctx=Load()), body=[Assign(targets=[Name(id='nbn_group', ctx=Store())], value=Call(func=Name(id='dict', ctx=Load()), args=[Name(id='group', ctx=Load())], keywords=[])), Assign(targets=[Name(id='bn_group', ctx=Store())], value=Call(func=Name(id='dict', ctx=Load()), args=[Name(id='group', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='bn_group', ctx=Load()), attr='update', ctx=Load()), args=[Name(id='bias_and_bn_params', ctx=Load())], keywords=[])), Assign(targets=[Subscript(value=Name(id='nbn_group', ctx=Load()), slice=Constant(value='params'), ctx=Store())], value=List(elts=[], ctx=Load())), Assign(targets=[Subscript(value=Name(id='bn_group', ctx=Load()), slice=Constant(value='params'), ctx=Store())], value=List(elts=[], ctx=Load())), For(target=Name(id='p', ctx=Store()), iter=Subscript(value=Name(id='group', ctx=Load()), slice=Constant(value='params'), ctx=Load()), body=[If(test=Compare(left=Attribute(value=Name(id='p', ctx=Load()), attr='ndim', ctx=Load()), ops=[Gt()], comparators=[Constant(value=1)]), body=[Expr(value=Call(func=Attribute(value=Subscript(value=Name(id='nbn_group', ctx=Load()), slice=Constant(value='params'), ctx=Load()), attr='append', ctx=Load()), args=[Name(id='p', ctx=Load())], keywords=[]))], orelse=[Expr(value=Call(func=Attribute(value=Subscript(value=Name(id='bn_group', ctx=Load()), slice=Constant(value='params'), ctx=Load()), attr='append', ctx=Load()), args=[Name(id='p', ctx=Load())], keywords=[]))])], orelse=[]), If(test=Subscript(value=Name(id='nbn_group', ctx=Load()), slice=Constant(value='params'), ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Name(id='new_parameters', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='nbn_group', ctx=Load())], keywords=[]))], orelse=[]), If(test=Subscript(value=Name(id='bn_group', ctx=Load()), slice=Constant(value='params'), ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Name(id='new_parameters', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='bn_group', ctx=Load())], keywords=[]))], orelse=[])], orelse=[]), Return(value=Name(id='new_parameters', ctx=Load()))], decorator_list=[Name(id='staticmethod', ctx=Load())])], decorator_list=[])], type_ignores=[])
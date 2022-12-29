Module(body=[Import(names=[alias(name='random')]), ImportFrom(module='contextlib', names=[alias(name='contextmanager')], level=0), Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='torch')]), ImportFrom(module='torch.nn.parallel', names=[alias(name='DataParallel'), alias(name='DistributedDataParallel')], level=0), Try(body=[Import(names=[alias(name='torch.cuda.amp')]), Assign(targets=[Name(id='USE_AMP', ctx=Store())], value=Constant(value=True))], handlers=[ExceptHandler(type=Name(id='ImportError', ctx=Load()), body=[Assign(targets=[Name(id='USE_AMP', ctx=Store())], value=Constant(value=False))])], orelse=[], finalbody=[]), FunctionDef(name='nullcontext', args=arguments(posonlyargs=[], args=[arg(arg='enter_result')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None)]), body=[Expr(value=Yield(value=Name(id='enter_result', ctx=Load())))], decorator_list=[Name(id='contextmanager', ctx=Load())]), FunctionDef(name='enable_amp', args=arguments(posonlyargs=[], args=[arg(arg='enable')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=True)]), body=[Expr(value=Constant(value='Context to disable AMP.')), If(test=BoolOp(op=And(), values=[Name(id='USE_AMP', ctx=Load()), Name(id='enable', ctx=Load())]), body=[Return(value=Call(func=Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='cuda', ctx=Load()), attr='amp', ctx=Load()), attr='autocast', ctx=Load()), args=[], keywords=[]))], orelse=[Return(value=Call(func=Name(id='nullcontext', ctx=Load()), args=[], keywords=[]))])], decorator_list=[]), FunctionDef(name='disable_amp', args=arguments(posonlyargs=[], args=[arg(arg='disable')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=True)]), body=[Expr(value=Constant(value='Context to disable AMP.')), If(test=BoolOp(op=And(), values=[Name(id='USE_AMP', ctx=Load()), Name(id='disable', ctx=Load())]), body=[Return(value=Call(func=Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='cuda', ctx=Load()), attr='amp', ctx=Load()), attr='autocast', ctx=Load()), args=[], keywords=[keyword(arg='enabled', value=Constant(value=False))]))], orelse=[Return(value=Call(func=Name(id='nullcontext', ctx=Load()), args=[], keywords=[]))])], decorator_list=[]), FunctionDef(name='tmp_seed', args=arguments(posonlyargs=[], args=[arg(arg='seed')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Centext manager for temporary random seed (random and Numpy modules).')), Assign(targets=[Name(id='state', ctx=Store())], value=Call(func=Attribute(value=Name(id='random', ctx=Load()), attr='getstate', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='np_state', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='get_state', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='torch_state', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='get_rng_state', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='random', ctx=Load()), attr='seed', ctx=Load()), args=[Name(id='seed', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='seed', ctx=Load()), args=[Name(id='seed', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='manual_seed', ctx=Load()), args=[Name(id='seed', ctx=Load())], keywords=[])), Try(body=[Expr(value=Yield(value=Constant(value=None)))], handlers=[], orelse=[], finalbody=[Expr(value=Call(func=Attribute(value=Name(id='random', ctx=Load()), attr='setstate', ctx=Load()), args=[Name(id='state', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='set_state', ctx=Load()), args=[Name(id='np_state', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='set_rng_state', ctx=Load()), args=[Name(id='torch_state', ctx=Load())], keywords=[]))])], decorator_list=[Name(id='contextmanager', ctx=Load())]), FunctionDef(name='get_base_module', args=arguments(posonlyargs=[], args=[arg(arg='module')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Returns base torch module from wappers like DP and DDP.')), If(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='module', ctx=Load()), Tuple(elts=[Name(id='DataParallel', ctx=Load()), Name(id='DistributedDataParallel', ctx=Load())], ctx=Load())], keywords=[]), body=[Assign(targets=[Name(id='module', ctx=Store())], value=Attribute(value=Name(id='module', ctx=Load()), attr='module', ctx=Load()))], orelse=[]), Return(value=Name(id='module', ctx=Load()))], decorator_list=[]), FunctionDef(name='freeze', args=arguments(posonlyargs=[], args=[arg(arg='model'), arg(arg='freeze')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=True)]), body=[Expr(value=Constant(value='Freeze or unfreeze all parameters of the model.')), For(target=Name(id='p', ctx=Store()), iter=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='parameters', ctx=Load()), args=[], keywords=[]), body=[Assign(targets=[Attribute(value=Name(id='p', ctx=Load()), attr='requires_grad', ctx=Store())], value=UnaryOp(op=Not(), operand=Name(id='freeze', ctx=Load())))], orelse=[])], decorator_list=[]), FunctionDef(name='freeze_bn', args=arguments(posonlyargs=[], args=[arg(arg='model'), arg(arg='freeze')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=True)]), body=[Expr(value=Constant(value='Freeze or unfreeze batchnorm parameters.')), If(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='model', ctx=Load()), Tuple(elts=[Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='BatchNorm2d', ctx=Load()), Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='BatchNorm1d', ctx=Load())], ctx=Load())], keywords=[]), body=[For(target=Name(id='p', ctx=Store()), iter=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='parameters', ctx=Load()), args=[], keywords=[]), body=[Assign(targets=[Attribute(value=Name(id='p', ctx=Load()), attr='requires_grad', ctx=Store())], value=UnaryOp(op=Not(), operand=Name(id='freeze', ctx=Load())))], orelse=[])], orelse=[]), For(target=Name(id='child', ctx=Store()), iter=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='children', ctx=Load()), args=[], keywords=[]), body=[Expr(value=Call(func=Name(id='freeze_bn', ctx=Load()), args=[Name(id='child', ctx=Load())], keywords=[keyword(arg='freeze', value=Name(id='freeze', ctx=Load()))]))], orelse=[])], decorator_list=[]), FunctionDef(name='eval_bn', args=arguments(posonlyargs=[], args=[arg(arg='model'), arg(arg='eval')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=True)]), body=[Expr(value=Constant(value='Change evaluation mode for model batchnorms.')), If(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='model', ctx=Load()), Tuple(elts=[Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='BatchNorm2d', ctx=Load()), Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='nn', ctx=Load()), attr='BatchNorm1d', ctx=Load())], ctx=Load())], keywords=[]), body=[Expr(value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='train', ctx=Load()), args=[UnaryOp(op=Not(), operand=Name(id='eval', ctx=Load()))], keywords=[]))], orelse=[]), For(target=Name(id='child', ctx=Store()), iter=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='children', ctx=Load()), args=[], keywords=[]), body=[Expr(value=Call(func=Name(id='eval_bn', ctx=Load()), args=[Name(id='child', ctx=Load())], keywords=[keyword(arg='eval', value=Name(id='eval', ctx=Load()))]))], orelse=[])], decorator_list=[]), FunctionDef(name='try_cuda', args=arguments(posonlyargs=[], args=[arg(arg='m')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='cuda', ctx=Load()), attr='is_available', ctx=Load()), args=[], keywords=[]), body=[Return(value=Call(func=Attribute(value=Name(id='m', ctx=Load()), attr='cuda', ctx=Load()), args=[], keywords=[]))], orelse=[]), Return(value=Name(id='m', ctx=Load()))], decorator_list=[])], type_ignores=[])
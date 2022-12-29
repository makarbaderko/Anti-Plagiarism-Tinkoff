Module(body=[Import(names=[alias(name='tempfile')]), Import(names=[alias(name='torch')]), ImportFrom(module='runner', names=[alias(name='Runner')], level=2), ImportFrom(module='common', names=[alias(name='setup')], level=1), FunctionDef(name='trace_embedder', args=arguments(posonlyargs=[], args=[arg(arg='arg')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Call(func=Name(id='setup', ctx=Load()), args=[], keywords=[])), If(test=Compare(left=Attribute(value=Name(id='arg', ctx=Load()), attr='checkpoint', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Input checkpoint path must be provided')], keywords=[]))], orelse=[]), If(test=Compare(left=Attribute(value=Name(id='arg', ctx=Load()), attr='trace_output', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Output checkpoint path must be provided')], keywords=[]))], orelse=[]), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='tempfile', ctx=Load()), attr='TemporaryDirectory', ctx=Load()), args=[], keywords=[]), optional_vars=Name(id='root', ctx=Store()))], body=[Assign(targets=[Name(id='runner', ctx=Store())], value=Call(func=Name(id='Runner', ctx=Load()), args=[Name(id='root', ctx=Load()), Attribute(value=Name(id='arg', ctx=Load()), attr='data', ctx=Load())], keywords=[keyword(arg='config', value=Attribute(value=Name(id='arg', ctx=Load()), attr='config', ctx=Load())), keyword(arg='logger', value=Constant(value='tensorboard')), keyword(arg='initial_checkpoint', value=Attribute(value=Name(id='arg', ctx=Load()), attr='checkpoint', ctx=Load())), keyword(arg='no_strict_init', value=Attribute(value=Name(id='arg', ctx=Load()), attr='no_strict_init', ctx=Load()))])), Expr(value=Call(func=Attribute(value=Name(id='runner', ctx=Load()), attr='init_stage', ctx=Load()), args=[Attribute(value=Name(id='runner', ctx=Load()), attr='STAGE_TEST', ctx=Load())], keywords=[])), Assign(targets=[Name(id='model', ctx=Store())], value=Subscript(value=Call(func=Attribute(value=Name(id='runner', ctx=Load()), attr='get_model', ctx=Load()), args=[Attribute(value=Name(id='runner', ctx=Load()), attr='STAGE_TEST', ctx=Load())], keywords=[]), slice=Constant(value='embedder'), ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='eval', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='loader', ctx=Store())], value=Call(func=Name(id='next', ctx=Load()), args=[Call(func=Name(id='it_er', ctx=Load()), args=[Call(func=Attribute(value=Call(func=Attribute(value=Name(id='runner', ctx=Load()), attr='get_loaders', ctx=Load()), args=[Attribute(value=Name(id='runner', ctx=Load()), attr='STAGE_TEST', ctx=Load())], keywords=[]), attr='values', ctx=Load()), args=[], keywords=[])], keywords=[])], keywords=[])), Assign(targets=[Name(id='batchH', ctx=Store())], value=Subscript(value=Call(func=Name(id='next', ctx=Load()), args=[Call(func=Name(id='it_er', ctx=Load()), args=[Name(id='loader', ctx=Load())], keywords=[])], keywords=[]), slice=Constant(value=0), ctx=Load())), If(test=UnaryOp(op=Not(), operand=Call(func=Name(id='isinstanc_e', ctx=Load()), args=[Name(id='batchH', ctx=Load()), Attribute(value=Name(id='torch', ctx=Load()), attr='Tensor', ctx=Load())], keywords=[])), body=[Assign(targets=[Name(id='batchH', ctx=Store())], value=Subscript(value=Name(id='batchH', ctx=Load()), slice=Constant(value=0), ctx=Load()))], orelse=[]), If(test=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='cuda', ctx=Load()), attr='is_available', ctx=Load()), args=[], keywords=[]), body=[Assign(targets=[Name(id='batchH', ctx=Store())], value=Call(func=Attribute(value=Name(id='batchH', ctx=Load()), attr='cuda', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='model', ctx=Store())], value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='cuda', ctx=Load()), args=[], keywords=[]))], orelse=[]), Assign(targets=[Name(id='checkpoint', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='jit', ctx=Load()), attr='trace', ctx=Load()), args=[Name(id='model', ctx=Load()), Name(id='batchH', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='jit', ctx=Load()), attr='save', ctx=Load()), args=[Name(id='checkpoint', ctx=Load()), Attribute(value=Name(id='arg', ctx=Load()), attr='trace_output', ctx=Load())], keywords=[]))])], decorator_list=[])], type_ignores=[])
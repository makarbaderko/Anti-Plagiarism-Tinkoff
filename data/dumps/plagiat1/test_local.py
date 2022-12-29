Module(body=[ImportFrom(module='functools', names=[alias(name='partial')], level=0), Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pytest')]), ImportFrom(module='etna.auto.runner', names=[alias(name='LocalRunner')], level=0), ImportFrom(module='etna.auto.runner', names=[alias(name='ParallelLocalRunner')], level=0), FunctionDef(name='payload', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='func', ctx=Store())], value=Call(func=Name(id='partial', ctx=Load()), args=[Attribute(value=Name(id='np', ctx=Load()), attr='einsum', ctx=Load()), Constant(value='ni,im->nm')], keywords=[])), Assign(targets=[Name(id='args', ctx=Store())], value=Tuple(elts=[Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='normal', ctx=Load()), args=[], keywords=[keyword(arg='size', value=Tuple(elts=[Constant(value=10), Constant(value=20)], ctx=Load()))]), Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='normal', ctx=Load()), args=[], keywords=[keyword(arg='size', value=Tuple(elts=[Constant(value=20), Constant(value=5)], ctx=Load()))])], ctx=Load())), Return(value=Tuple(elts=[Name(id='func', ctx=Load()), Name(id='args', ctx=Load())], ctx=Load()))], decorator_list=[Call(func=Attribute(value=Name(id='pytest', ctx=Load()), attr='fixture', ctx=Load()), args=[], keywords=[])]), FunctionDef(name='test_run_local_runner', args=arguments(posonlyargs=[], args=[arg(arg='payload')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='                  ')), Assign(targets=[Tuple(elts=[Name(id='func', ctx=Store()), Name(id='args', ctx=Store())], ctx=Store())], value=Name(id='payload', ctx=Load())), Assign(targets=[Name(id='runner', ctx=Store())], value=Call(func=Name(id='LocalRunner', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='result', ctx=Store())], value=Call(func=Name(id='runner', ctx=Load()), args=[Name(id='func', ctx=Load()), Starred(value=Name(id='args', ctx=Load()), ctx=Load())], keywords=[])), Assert(test=Compare(left=Attribute(value=Name(id='result', ctx=Load()), attr='shape', ctx=Load()), ops=[Eq()], comparators=[Tuple(elts=[Subscript(value=Attribute(value=Subscript(value=Name(id='args', ctx=Load()), slice=Constant(value=0), ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=0), ctx=Load()), Subscript(value=Attribute(value=Subscript(value=Name(id='args', ctx=Load()), slice=Constant(value=1), ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=1), ctx=Load())], ctx=Load())]))], decorator_list=[]), FunctionDef(name='test_run_parallel_local_runner', args=arguments(posonlyargs=[], args=[arg(arg='payload')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='͜˃ǀ ä    ')), Assign(targets=[Tuple(elts=[Name(id='func', ctx=Store()), Name(id='args', ctx=Store())], ctx=Store())], value=Name(id='payload', ctx=Load())), Assign(targets=[Name(id='n_jobs', ctx=Store())], value=Constant(value=4)), Assign(targets=[Name(id='runner', ctx=Store())], value=Call(func=Name(id='ParallelLocalRunner', ctx=Load()), args=[], keywords=[keyword(arg='n_jobs', value=Name(id='n_jobs', ctx=Load()))])), Assign(targets=[Name(id='result', ctx=Store())], value=Call(func=Name(id='runner', ctx=Load()), args=[Name(id='func', ctx=Load()), Starred(value=Name(id='args', ctx=Load()), ctx=Load())], keywords=[])), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='result', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Name(id='n_jobs', ctx=Load())])), For(target=Name(id='res', ctx=Store()), iter=Name(id='result', ctx=Load()), body=[Assert(test=Compare(left=Attribute(value=Name(id='res', ctx=Load()), attr='shape', ctx=Load()), ops=[Eq()], comparators=[Tuple(elts=[Subscript(value=Attribute(value=Subscript(value=Name(id='args', ctx=Load()), slice=Constant(value=0), ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=0), ctx=Load()), Subscript(value=Attribute(value=Subscript(value=Name(id='args', ctx=Load()), slice=Constant(value=1), ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=1), ctx=Load())], ctx=Load())]))], orelse=[])], decorator_list=[])], type_ignores=[])
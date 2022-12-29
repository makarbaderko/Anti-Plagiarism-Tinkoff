Module(body=[Import(names=[alias(name='itertools')]), Import(names=[alias(name='math')]), ImportFrom(module='probabilistic_embeddings.layers.distribution.common', names=[alias(name='auto_matmul')], level=0), Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='torch')]), ImportFrom(module='unittest', names=[alias(name='TestCase'), alias(name='main')], level=0), ClassDef(name='T_estCommon', bases=[Name(id='TestCase', ctx=Load())], keywords=[], body=[FunctionDef(name='test_auto_matm', args=arguments(posonlyargs=[], args=[arg(arg='SELF')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[FunctionDef(name='_check_case', args=arguments(posonlyargs=[], args=[arg(arg='shape1'), arg(arg='s_hape2')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='  ίǴ Ƚ ¤  ƛĒ  ̅ 9  r  ͑ ̘  ėc& ')), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='no_grad', ctx=Load()), args=[], keywords=[]))], body=[Assign(targets=[Name(id='mt', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='randn', ctx=Load()), args=[Starred(value=Name(id='shape1', ctx=Load()), ctx=Load())], keywords=[])), Assign(targets=[Name(id='m', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='randn', ctx=Load()), args=[Starred(value=Name(id='s_hape2', ctx=Load()), ctx=Load())], keywords=[])), Assign(targets=[Name(id='gt', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='matmul', ctx=Load()), args=[Name(id='mt', ctx=Load()), Name(id='m', ctx=Load())], keywords=[]), attr='numpy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='resultiDW', ctx=Store())], value=Call(func=Attribute(value=Call(func=Name(id='auto_matmul', ctx=Load()), args=[Name(id='mt', ctx=Load()), Name(id='m', ctx=Load())], keywords=[]), attr='numpy', ctx=Load()), args=[], keywords=[]))]), Expr(value=Call(func=Attribute(value=Name(id='SELF', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='allclose', ctx=Load()), args=[Name(id='resultiDW', ctx=Load()), Name(id='gt', ctx=Load())], keywords=[keyword(arg='atol', value=Constant(value=1e-06))])], keywords=[]))], decorator_list=[]), Expr(value=Call(func=Name(id='_check_case', ctx=Load()), args=[List(elts=[Constant(value=0), Constant(value=1)], ctx=Load()), List(elts=[Constant(value=1), Constant(value=2)], ctx=Load())], keywords=[])), Expr(value=Call(func=Name(id='_check_case', ctx=Load()), args=[List(elts=[Constant(value=5), Constant(value=1), Constant(value=4), Constant(value=1), Constant(value=7)], ctx=Load()), List(elts=[Constant(value=2), Constant(value=4), Constant(value=7), Constant(value=2)], ctx=Load())], keywords=[])), Expr(value=Call(func=Name(id='_check_case', ctx=Load()), args=[List(elts=[Constant(value=3), Constant(value=2), Constant(value=1), Constant(value=4), Constant(value=5)], ctx=Load()), List(elts=[Constant(value=1), Constant(value=6), Constant(value=5), Constant(value=1)], ctx=Load())], keywords=[]))], decorator_list=[])], decorator_list=[]), If(test=Compare(left=Name(id='__name__', ctx=Load()), ops=[Eq()], comparators=[Constant(value='__main__')]), body=[Expr(value=Call(func=Name(id='main', ctx=Load()), args=[], keywords=[]))], orelse=[])], type_ignores=[])
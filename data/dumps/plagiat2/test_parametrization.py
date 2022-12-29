Module(body=[Import(names=[alias(name='itertools')]), Import(names=[alias(name='math')]), ImportFrom(module='unittest', names=[alias(name='TestCase'), alias(name='main')], level=0), Import(names=[alias(name='numpy', asname='np')]), ImportFrom(module='probabilistic_embeddings.layers.parametrization', names=[alias(name='Parametrization')], level=0), Import(names=[alias(name='torch')]), ClassDef(name='TestParametrization', bases=[Name(id='TestCase', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='ğ͇   Èβ  2ȑɮ  \x8d   µŃ Ȟ')), FunctionDef(name='test_log_positive', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' Ǖ  \u0378 ŌȚ  ŷʒ   /')), For(target=Name(id='type', ctx=Store()), iter=List(elts=[Constant(value='exp'), Constant(value='invlin'), Constant(value='abs')], ctx=Load()), body=[For(target=Name(id='min', ctx=Store()), iter=List(elts=[Constant(value=0), Constant(value=0.1), Constant(value=1), Constant(value=10)], ctx=Load()), body=[For(target=Name(id='kwargs', ctx=Store()), iter=List(elts=[Dict(keys=[Constant(value='scale'), Constant(value='center')], values=[Constant(value=1), Constant(value=0)]), Dict(keys=[Constant(value='scale'), Constant(value='center')], values=[Constant(value=0.3), Constant(value=5.4)])], ctx=Load()), body=[Assign(targets=[Name(id='p', ctx=Store())], value=Call(func=Name(id='Parametrization', ctx=Load()), args=[], keywords=[keyword(arg='type', value=Name(id='type', ctx=Load())), keyword(arg='min', value=Name(id='min', ctx=Load())), keyword(value=Name(id='kwargs', ctx=Load()))])), Assign(targets=[Name(id='XS', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='linspace', ctx=Load()), args=[UnaryOp(op=USub(), operand=Constant(value=10)), Constant(value=10), Constant(value=1001)], keywords=[])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='no_grad', ctx=Load()), args=[], keywords=[]))], body=[Assign(targets=[Name(id='ys_gtTZeRb', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='p', ctx=Load()), attr='positive', ctx=Load()), args=[Name(id='XS', ctx=Load())], keywords=[]), attr='log', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='ys', ctx=Store())], value=Call(func=Attribute(value=Name(id='p', ctx=Load()), attr='log_positive', ctx=Load()), args=[Name(id='XS', ctx=Load())], keywords=[]))]), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='allclose', ctx=Load()), args=[Call(func=Attribute(value=Name(id='ys', ctx=Load()), attr='numpy', ctx=Load()), args=[], keywords=[]), Call(func=Attribute(value=Name(id='ys_gtTZeRb', ctx=Load()), attr='numpy', ctx=Load()), args=[], keywords=[])], keywords=[keyword(arg='atol', value=Constant(value=1e-06))])], keywords=[]))], orelse=[])], orelse=[])], orelse=[]), For(target=Name(id='max_', ctx=Store()), iter=List(elts=[Constant(value=0), Constant(value=0.1), Constant(value=1), Constant(value=10)], ctx=Load()), body=[For(target=Name(id='min', ctx=Store()), iter=List(elts=[Constant(value=0), Constant(value=0.1), Constant(value=1), Constant(value=10)], ctx=Load()), body=[If(test=Compare(left=Name(id='min', ctx=Load()), ops=[GtE()], comparators=[Name(id='max_', ctx=Load())]), body=[Continue()], orelse=[]), Assign(targets=[Name(id='p', ctx=Store())], value=Call(func=Name(id='Parametrization', ctx=Load()), args=[], keywords=[keyword(arg='type', value=Constant(value='sigmoid')), keyword(arg='min', value=Name(id='min', ctx=Load())), keyword(arg='max', value=Name(id='max_', ctx=Load()))])), Assign(targets=[Name(id='XS', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='linspace', ctx=Load()), args=[UnaryOp(op=USub(), operand=Constant(value=10)), Constant(value=10), Constant(value=1001)], keywords=[])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='no_grad', ctx=Load()), args=[], keywords=[]))], body=[Assign(targets=[Name(id='ys_gtTZeRb', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='p', ctx=Load()), attr='positive', ctx=Load()), args=[Name(id='XS', ctx=Load())], keywords=[]), attr='log', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='ys', ctx=Store())], value=Call(func=Attribute(value=Name(id='p', ctx=Load()), attr='log_positive', ctx=Load()), args=[Name(id='XS', ctx=Load())], keywords=[]))]), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='allclose', ctx=Load()), args=[Call(func=Attribute(value=Name(id='ys', ctx=Load()), attr='numpy', ctx=Load()), args=[], keywords=[]), Call(func=Attribute(value=Name(id='ys_gtTZeRb', ctx=Load()), attr='numpy', ctx=Load()), args=[], keywords=[])], keywords=[keyword(arg='atol', value=Constant(value=1e-06))])], keywords=[]))], orelse=[])], orelse=[])], decorator_list=[]), FunctionDef(name='test_ipositive', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[For(target=Name(id='type', ctx=Store()), iter=List(elts=[Constant(value='exp'), Constant(value='invlin')], ctx=Load()), body=[For(target=Name(id='min', ctx=Store()), iter=List(elts=[Constant(value=0), Constant(value=0.1), Constant(value=1), Constant(value=10)], ctx=Load()), body=[For(target=Name(id='kwargs', ctx=Store()), iter=List(elts=[Dict(keys=[Constant(value='scale'), Constant(value='center')], values=[Constant(value=1), Constant(value=0)]), Dict(keys=[Constant(value='scale'), Constant(value='center')], values=[Constant(value=0.3), Constant(value=0.9)])], ctx=Load()), body=[Assign(targets=[Name(id='p', ctx=Store())], value=Call(func=Name(id='Parametrization', ctx=Load()), args=[], keywords=[keyword(arg='type', value=Name(id='type', ctx=Load())), keyword(arg='min', value=Name(id='min', ctx=Load())), keyword(value=Name(id='kwargs', ctx=Load()))])), Assign(targets=[Name(id='xs_', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='linspace', ctx=Load()), args=[UnaryOp(op=USub(), operand=Constant(value=5)), Constant(value=5), Constant(value=1001)], keywords=[]), attr='double', ctx=Load()), args=[], keywords=[])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='no_grad', ctx=Load()), args=[], keywords=[]))], body=[Assign(targets=[Name(id='ys', ctx=Store())], value=Call(func=Attribute(value=Name(id='p', ctx=Load()), attr='positive', ctx=Load()), args=[Name(id='xs_', ctx=Load())], keywords=[])), Assign(targets=[Name(id='XS', ctx=Store())], value=Call(func=Attribute(value=Name(id='p', ctx=Load()), attr='ipositive', ctx=Load()), args=[Name(id='ys', ctx=Load())], keywords=[]))]), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Compare(left=Name(id='ys', ctx=Load()), ops=[Gt()], comparators=[Constant(value=0)]), attr='all', ctx=Load()), args=[], keywords=[])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='allclose', ctx=Load()), args=[Call(func=Attribute(value=Name(id='XS', ctx=Load()), attr='numpy', ctx=Load()), args=[], keywords=[]), Call(func=Attribute(value=Name(id='xs_', ctx=Load()), attr='numpy', ctx=Load()), args=[], keywords=[])], keywords=[keyword(arg='atol', value=Constant(value=1e-06))])], keywords=[]))], orelse=[])], orelse=[])], orelse=[]), For(target=Name(id='max_', ctx=Store()), iter=List(elts=[Constant(value=0), Constant(value=0.1), Constant(value=1), Constant(value=10)], ctx=Load()), body=[For(target=Name(id='min', ctx=Store()), iter=List(elts=[Constant(value=0), Constant(value=0.1), Constant(value=1), Constant(value=10)], ctx=Load()), body=[If(test=Compare(left=Name(id='min', ctx=Load()), ops=[GtE()], comparators=[Name(id='max_', ctx=Load())]), body=[Continue()], orelse=[]), Assign(targets=[Name(id='p', ctx=Store())], value=Call(func=Name(id='Parametrization', ctx=Load()), args=[], keywords=[keyword(arg='type', value=Constant(value='sigmoid')), keyword(arg='min', value=Name(id='min', ctx=Load())), keyword(arg='max', value=Name(id='max_', ctx=Load()))])), Assign(targets=[Name(id='xs_', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='linspace', ctx=Load()), args=[UnaryOp(op=USub(), operand=Constant(value=10)), Constant(value=10), Constant(value=1001)], keywords=[]), attr='double', ctx=Load()), args=[], keywords=[])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='no_grad', ctx=Load()), args=[], keywords=[]))], body=[Assign(targets=[Name(id='ys', ctx=Store())], value=Call(func=Attribute(value=Name(id='p', ctx=Load()), attr='positive', ctx=Load()), args=[Name(id='xs_', ctx=Load())], keywords=[])), Assign(targets=[Name(id='XS', ctx=Store())], value=Call(func=Attribute(value=Name(id='p', ctx=Load()), attr='ipositive', ctx=Load()), args=[Name(id='ys', ctx=Load())], keywords=[]))]), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Compare(left=Name(id='ys', ctx=Load()), ops=[Gt()], comparators=[Constant(value=0)]), attr='all', ctx=Load()), args=[], keywords=[])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='allclose', ctx=Load()), args=[Call(func=Attribute(value=Name(id='XS', ctx=Load()), attr='numpy', ctx=Load()), args=[], keywords=[]), Call(func=Attribute(value=Name(id='xs_', ctx=Load()), attr='numpy', ctx=Load()), args=[], keywords=[])], keywords=[keyword(arg='atol', value=Constant(value=1e-06))])], keywords=[]))], orelse=[])], orelse=[]), For(target=Name(id='min', ctx=Store()), iter=List(elts=[Constant(value=0), Constant(value=0.1), Constant(value=1), Constant(value=10)], ctx=Load()), body=[Assign(targets=[Name(id='p', ctx=Store())], value=Call(func=Name(id='Parametrization', ctx=Load()), args=[], keywords=[keyword(arg='type', value=Constant(value='abs')), keyword(arg='min', value=Name(id='min', ctx=Load()))])), Assign(targets=[Name(id='xs_', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='linspace', ctx=Load()), args=[Constant(value=0), Constant(value=5), Constant(value=1001)], keywords=[]), attr='double', ctx=Load()), args=[], keywords=[])), With(items=[withitem(context_expr=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='no_grad', ctx=Load()), args=[], keywords=[]))], body=[Assign(targets=[Name(id='ys', ctx=Store())], value=Call(func=Attribute(value=Name(id='p', ctx=Load()), attr='positive', ctx=Load()), args=[Name(id='xs_', ctx=Load())], keywords=[])), Assign(targets=[Name(id='XS', ctx=Store())], value=Call(func=Attribute(value=Name(id='p', ctx=Load()), attr='ipositive', ctx=Load()), args=[Name(id='ys', ctx=Load())], keywords=[]))]), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Compare(left=Name(id='ys', ctx=Load()), ops=[GtE()], comparators=[Constant(value=0)]), attr='all', ctx=Load()), args=[], keywords=[])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='allclose', ctx=Load()), args=[Call(func=Attribute(value=Name(id='XS', ctx=Load()), attr='numpy', ctx=Load()), args=[], keywords=[]), Call(func=Attribute(value=Name(id='xs_', ctx=Load()), attr='numpy', ctx=Load()), args=[], keywords=[])], keywords=[keyword(arg='atol', value=Constant(value=1e-06))])], keywords=[]))], orelse=[])], decorator_list=[])], decorator_list=[]), If(test=Compare(left=Name(id='__name__', ctx=Load()), ops=[Eq()], comparators=[Constant(value='__main__')]), body=[Expr(value=Call(func=Name(id='main', ctx=Load()), args=[], keywords=[]))], orelse=[])], type_ignores=[])
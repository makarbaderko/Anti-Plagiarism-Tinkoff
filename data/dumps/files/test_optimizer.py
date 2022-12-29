Module(body=[Import(names=[alias(name='os')]), Import(names=[alias(name='tempfile')]), ImportFrom(module='collections', names=[alias(name='OrderedDict')], level=0), ImportFrom(module='unittest', names=[alias(name='TestCase'), alias(name='main')], level=0), ImportFrom(module='probabilistic_embeddings.trainer.optimizer', names=[alias(name='*')], level=0), ClassDef(name='TestOptimizer', bases=[Name(id='TestCase', ctx=Load())], keywords=[], body=[FunctionDef(name='test_sam_split', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='parameters', ctx=Store())], value=List(elts=[Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='full', ctx=Load()), args=[List(elts=[], ctx=Load()), Constant(value=2.0)], keywords=[]), Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='full', ctx=Load()), args=[List(elts=[Constant(value=5), Constant(value=3)], ctx=Load()), Constant(value=2.0)], keywords=[]), Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='full', ctx=Load()), args=[List(elts=[Constant(value=5)], ctx=Load()), Constant(value=2.0)], keywords=[])], ctx=Load())), Assign(targets=[Name(id='groups', ctx=Store())], value=Call(func=Attribute(value=Name(id='SamOptimizer', ctx=Load()), attr='_split_bias_and_bn_groups', ctx=Load()), args=[Name(id='parameters', ctx=Load()), Dict(keys=[Constant(value='adaptive')], values=[Constant(value=False)])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertEqual', ctx=Load()), args=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='groups', ctx=Load())], keywords=[]), Constant(value=2)], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertEqual', ctx=Load()), args=[Call(func=Name(id='len', ctx=Load()), args=[Subscript(value=Name(id='groups', ctx=Load()), slice=Constant(value=0), ctx=Load())], keywords=[]), Constant(value=1)], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertEqual', ctx=Load()), args=[Call(func=Name(id='len', ctx=Load()), args=[Subscript(value=Name(id='groups', ctx=Load()), slice=Constant(value=1), ctx=Load())], keywords=[]), Constant(value=2)], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertEqual', ctx=Load()), args=[Attribute(value=Subscript(value=Subscript(value=Subscript(value=Name(id='groups', ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value='params'), ctx=Load()), slice=Constant(value=0), ctx=Load()), attr='ndim', ctx=Load()), Constant(value=2)], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertEqual', ctx=Load()), args=[Attribute(value=Subscript(value=Subscript(value=Subscript(value=Name(id='groups', ctx=Load()), slice=Constant(value=1), ctx=Load()), slice=Constant(value='params'), ctx=Load()), slice=Constant(value=0), ctx=Load()), attr='ndim', ctx=Load()), Constant(value=0)], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertEqual', ctx=Load()), args=[Attribute(value=Subscript(value=Subscript(value=Subscript(value=Name(id='groups', ctx=Load()), slice=Constant(value=1), ctx=Load()), slice=Constant(value='params'), ctx=Load()), slice=Constant(value=1), ctx=Load()), attr='ndim', ctx=Load()), Constant(value=1)], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertEqual', ctx=Load()), args=[Subscript(value=Subscript(value=Name(id='groups', ctx=Load()), slice=Constant(value=1), ctx=Load()), slice=Constant(value='adaptive'), ctx=Load()), Constant(value=False)], keywords=[])), FunctionDef(name='closure', args=arguments(posonlyargs=[], args=[arg(arg='optimizer')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[For(target=Name(id='group', ctx=Store()), iter=Attribute(value=Name(id='optimizer', ctx=Load()), attr='param_groups', ctx=Load()), body=[For(target=Name(id='p', ctx=Store()), iter=Subscript(value=Name(id='group', ctx=Load()), slice=Constant(value='params'), ctx=Load()), body=[Assign(targets=[Attribute(value=Name(id='p', ctx=Load()), attr='grad', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='ones_like', ctx=Load()), args=[Name(id='p', ctx=Load())], keywords=[]))], orelse=[])], orelse=[])], decorator_list=[]), Assign(targets=[Name(id='optimizer', ctx=Store())], value=Call(func=Name(id='SamOptimizer', ctx=Load()), args=[ListComp(elt=Call(func=Attribute(value=Name(id='p', ctx=Load()), attr='clone', ctx=Load()), args=[], keywords=[]), generators=[comprehension(target=Name(id='p', ctx=Store()), iter=Name(id='parameters', ctx=Load()), ifs=[], is_async=0)])], keywords=[keyword(arg='config', value=Dict(keys=[Constant(value='adaptive_bias_and_bn')], values=[Constant(value=True)]))])), Expr(value=Call(func=Name(id='closure', ctx=Load()), args=[Name(id='optimizer', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='optimizer', ctx=Load()), attr='first_step', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertFalse', ctx=Load()), args=[Call(func=Attribute(value=Subscript(value=Subscript(value=Subscript(value=Attribute(value=Name(id='optimizer', ctx=Load()), attr='param_groups', ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value='params'), ctx=Load()), slice=Constant(value=0), ctx=Load()), attr='allclose', ctx=Load()), args=[Subscript(value=Name(id='parameters', ctx=Load()), slice=Constant(value=0), ctx=Load())], keywords=[])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertFalse', ctx=Load()), args=[Call(func=Attribute(value=Subscript(value=Subscript(value=Subscript(value=Attribute(value=Name(id='optimizer', ctx=Load()), attr='param_groups', ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value='params'), ctx=Load()), slice=Constant(value=1), ctx=Load()), attr='allclose', ctx=Load()), args=[Subscript(value=Name(id='parameters', ctx=Load()), slice=Constant(value=1), ctx=Load())], keywords=[])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertFalse', ctx=Load()), args=[Call(func=Attribute(value=Subscript(value=Subscript(value=Subscript(value=Attribute(value=Name(id='optimizer', ctx=Load()), attr='param_groups', ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value='params'), ctx=Load()), slice=Constant(value=2), ctx=Load()), attr='allclose', ctx=Load()), args=[Subscript(value=Name(id='parameters', ctx=Load()), slice=Constant(value=2), ctx=Load())], keywords=[])], keywords=[])), Assign(targets=[Name(id='gt_update', ctx=Store())], value=Subscript(value=Subscript(value=Attribute(value=Name(id='optimizer', ctx=Load()), attr='param_groups', ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value='params'), ctx=Load())), Assign(targets=[Name(id='optimizer', ctx=Store())], value=Call(func=Name(id='SamOptimizer', ctx=Load()), args=[ListComp(elt=Call(func=Attribute(value=Name(id='p', ctx=Load()), attr='clone', ctx=Load()), args=[], keywords=[]), generators=[comprehension(target=Name(id='p', ctx=Store()), iter=Name(id='parameters', ctx=Load()), ifs=[], is_async=0)])], keywords=[keyword(arg='config', value=Dict(keys=[Constant(value='adaptive_bias_and_bn')], values=[Constant(value=False)]))])), Expr(value=Call(func=Name(id='closure', ctx=Load()), args=[Name(id='optimizer', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='optimizer', ctx=Load()), attr='first_step', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Compare(left=Subscript(value=Subscript(value=Subscript(value=Attribute(value=Name(id='optimizer', ctx=Load()), attr='param_groups', ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value='params'), ctx=Load()), slice=Constant(value=0), ctx=Load()), ops=[Gt()], comparators=[Subscript(value=Name(id='gt_update', ctx=Load()), slice=Constant(value=1), ctx=Load())]), attr='all', ctx=Load()), args=[], keywords=[])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Compare(left=Subscript(value=Subscript(value=Subscript(value=Attribute(value=Name(id='optimizer', ctx=Load()), attr='param_groups', ctx=Load()), slice=Constant(value=1), ctx=Load()), slice=Constant(value='params'), ctx=Load()), slice=Constant(value=0), ctx=Load()), ops=[Lt()], comparators=[Subscript(value=Name(id='gt_update', ctx=Load()), slice=Constant(value=0), ctx=Load())]), attr='all', ctx=Load()), args=[], keywords=[])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertTrue', ctx=Load()), args=[Call(func=Attribute(value=Compare(left=Subscript(value=Subscript(value=Subscript(value=Attribute(value=Name(id='optimizer', ctx=Load()), attr='param_groups', ctx=Load()), slice=Constant(value=1), ctx=Load()), slice=Constant(value='params'), ctx=Load()), slice=Constant(value=1), ctx=Load()), ops=[Lt()], comparators=[Subscript(value=Name(id='gt_update', ctx=Load()), slice=Constant(value=2), ctx=Load())]), attr='all', ctx=Load()), args=[], keywords=[])], keywords=[]))], decorator_list=[])], decorator_list=[]), If(test=Compare(left=Name(id='__name__', ctx=Load()), ops=[Eq()], comparators=[Constant(value='__main__')]), body=[Expr(value=Call(func=Name(id='main', ctx=Load()), args=[], keywords=[]))], orelse=[])], type_ignores=[])
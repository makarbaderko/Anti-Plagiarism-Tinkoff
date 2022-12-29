Module(body=[Import(names=[alias(name='math')]), ImportFrom(module='unittest', names=[alias(name='TestCase'), alias(name='main')], level=0), Import(names=[alias(name='torch')]), ImportFrom(module='probabilistic_embeddings.criterion.multisim', names=[alias(name='MultiSimilarityLoss')], level=0), ImportFrom(module='probabilistic_embeddings.layers', names=[alias(name='DiracDistribution'), alias(name='NegativeL2Scorer')], level=0), ClassDef(name='TestMultiSimilarityLoss', bases=[Name(id='TestCase', ctx=Load())], keywords=[], body=[FunctionDef(name='test_1d', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='distribution', ctx=Store())], value=Call(func=Name(id='DiracDistribution', ctx=Load()), args=[], keywords=[keyword(arg='config', value=Dict(keys=[Constant(value='dim')], values=[Constant(value=1)]))])), Assign(targets=[Name(id='scorer', ctx=Store())], value=Call(func=Name(id='NegativeL2Scorer', ctx=Load()), args=[Name(id='distribution', ctx=Load())], keywords=[])), Assign(targets=[Name(id='multi_similarity_loss', ctx=Store())], value=Call(func=Name(id='MultiSimilarityLoss', ctx=Load()), args=[], keywords=[keyword(arg='aggregation', value=Constant(value='none'))])), Assign(targets=[Name(id='embeddings', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='tensor', ctx=Load()), args=[List(elts=[UnaryOp(op=USub(), operand=Constant(value=1)), Constant(value=0), Constant(value=2)], ctx=Load())], keywords=[]), attr='float', ctx=Load()), args=[], keywords=[]), attr='reshape', ctx=Load()), args=[UnaryOp(op=USub(), operand=Constant(value=1)), Constant(value=1)], keywords=[])), Assign(targets=[Name(id='labels', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='tensor', ctx=Load()), args=[List(elts=[Constant(value=0), Constant(value=1), Constant(value=0)], ctx=Load())], keywords=[])), Assign(targets=[Name(id='losses', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Name(id='multi_similarity_loss', ctx=Load()), args=[Name(id='embeddings', ctx=Load()), Name(id='labels', ctx=Load()), Name(id='scorer', ctx=Load())], keywords=[]), attr='numpy', ctx=Load()), args=[], keywords=[]), attr='tolist', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='losses_gt', ctx=Store())], value=List(elts=[BinOp(left=BinOp(left=BinOp(left=Constant(value=1), op=Div(), right=Constant(value=2)), op=Mult(), right=Call(func=Attribute(value=Name(id='math', ctx=Load()), attr='log', ctx=Load()), args=[BinOp(left=Constant(value=1), op=Add(), right=Call(func=Attribute(value=Name(id='math', ctx=Load()), attr='exp', ctx=Load()), args=[BinOp(left=UnaryOp(op=USub(), operand=Constant(value=2)), op=Mult(), right=UnaryOp(op=USub(), operand=Constant(value=9.5)))], keywords=[]))], keywords=[])), op=Add(), right=BinOp(left=BinOp(left=Constant(value=1), op=Div(), right=Constant(value=40)), op=Mult(), right=Call(func=Attribute(value=Name(id='math', ctx=Load()), attr='log', ctx=Load()), args=[BinOp(left=Constant(value=1), op=Add(), right=Call(func=Attribute(value=Name(id='math', ctx=Load()), attr='exp', ctx=Load()), args=[BinOp(left=Constant(value=40), op=Mult(), right=UnaryOp(op=USub(), operand=Constant(value=1.5)))], keywords=[]))], keywords=[]))), Constant(value=0), BinOp(left=BinOp(left=BinOp(left=Constant(value=1), op=Div(), right=Constant(value=2)), op=Mult(), right=Call(func=Attribute(value=Name(id='math', ctx=Load()), attr='log', ctx=Load()), args=[BinOp(left=Constant(value=1), op=Add(), right=Call(func=Attribute(value=Name(id='math', ctx=Load()), attr='exp', ctx=Load()), args=[BinOp(left=UnaryOp(op=USub(), operand=Constant(value=2)), op=Mult(), right=UnaryOp(op=USub(), operand=Constant(value=9.5)))], keywords=[]))], keywords=[])), op=Add(), right=BinOp(left=BinOp(left=Constant(value=1), op=Div(), right=Constant(value=40)), op=Mult(), right=Call(func=Attribute(value=Name(id='math', ctx=Load()), attr='log', ctx=Load()), args=[BinOp(left=Constant(value=1), op=Add(), right=Call(func=Attribute(value=Name(id='math', ctx=Load()), attr='exp', ctx=Load()), args=[BinOp(left=Constant(value=40), op=Mult(), right=UnaryOp(op=USub(), operand=Constant(value=4.5)))], keywords=[]))], keywords=[])))], ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertEqual', ctx=Load()), args=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='losses', ctx=Load())], keywords=[]), Constant(value=3)], keywords=[])), For(target=Tuple(elts=[Name(id='loss', ctx=Store()), Name(id='loss_gt', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='zip', ctx=Load()), args=[Name(id='losses', ctx=Load()), Name(id='losses_gt', ctx=Load())], keywords=[]), body=[Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertAlmostEqual', ctx=Load()), args=[Name(id='loss', ctx=Load()), Name(id='loss_gt', ctx=Load())], keywords=[]))], orelse=[])], decorator_list=[])], decorator_list=[]), If(test=Compare(left=Name(id='__name__', ctx=Load()), ops=[Eq()], comparators=[Constant(value='__main__')]), body=[Expr(value=Call(func=Name(id='main', ctx=Load()), args=[], keywords=[]))], orelse=[])], type_ignores=[])
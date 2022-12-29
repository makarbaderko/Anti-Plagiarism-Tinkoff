Module(body=[ImportFrom(module='unittest', names=[alias(name='TestCase'), alias(name='main')], level=0), Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='torch')]), ImportFrom(module='torchvision', names=[alias(name='transforms')], level=0), ImportFrom(module='probabilistic_embeddings.dataset', names=[alias(name='ImageTransform')], level=0), ImportFrom(module='probabilistic_embeddings.model', names=[alias(name='Model')], level=0), ClassDef(name='TestModel', bases=[Name(id='TestCase', ctx=Load())], keywords=[], body=[FunctionDef(name='test_forward', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Run forward for default model.')), Assign(targets=[Name(id='model', ctx=Store())], value=Call(func=Name(id='Model', ctx=Load()), args=[], keywords=[keyword(arg='num_classes', value=Constant(value=100))])), Assign(targets=[Name(id='image_transform', ctx=Store())], value=Call(func=Name(id='ImageTransform', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Attribute(value=Name(id='transforms', ctx=Load()), attr='Compose', ctx=Load()), args=[List(elts=[Call(func=Attribute(value=Name(id='transforms', ctx=Load()), attr='ToTensor', ctx=Load()), args=[], keywords=[]), Name(id='image_transform', ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='sample_input', ctx=Store())], value=Call(func=Attribute(value=BinOp(left=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='random', ctx=Load()), args=[Tuple(elts=[Constant(value=4), Attribute(value=Name(id='image_transform', ctx=Load()), attr='image_size', ctx=Load()), Attribute(value=Name(id='image_transform', ctx=Load()), attr='image_size', ctx=Load()), Constant(value=3)], ctx=Load())], keywords=[]), op=Mult(), right=Constant(value=255)), attr='astype', ctx=Load()), args=[Attribute(value=Name(id='np', ctx=Load()), attr='uint8', ctx=Load())], keywords=[])), Assign(targets=[Name(id='batch', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='stack', ctx=Load()), args=[Call(func=Name(id='list', ctx=Load()), args=[Call(func=Name(id='map', ctx=Load()), args=[Name(id='transform', ctx=Load()), Name(id='sample_input', ctx=Load())], keywords=[])], keywords=[])], keywords=[])), Assign(targets=[Name(id='logits', ctx=Store())], value=Subscript(value=Call(func=Name(id='model', ctx=Load()), args=[Name(id='batch', ctx=Load())], keywords=[]), slice=Constant(value='logits'), ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertEqual', ctx=Load()), args=[Attribute(value=Name(id='logits', ctx=Load()), attr='shape', ctx=Load()), Tuple(elts=[Constant(value=4), Constant(value=100)], ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='test_scoring', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Run scoring for default model.')), Assign(targets=[Name(id='model', ctx=Store())], value=Call(func=Name(id='Model', ctx=Load()), args=[], keywords=[keyword(arg='num_classes', value=Constant(value=100))])), Assign(targets=[Name(id='image_transform', ctx=Store())], value=Call(func=Name(id='ImageTransform', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='transform', ctx=Store())], value=Call(func=Attribute(value=Name(id='transforms', ctx=Load()), attr='Compose', ctx=Load()), args=[List(elts=[Call(func=Attribute(value=Name(id='transforms', ctx=Load()), attr='ToTensor', ctx=Load()), args=[], keywords=[]), Name(id='image_transform', ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='sample_input1', ctx=Store())], value=Call(func=Attribute(value=BinOp(left=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='random', ctx=Load()), args=[Tuple(elts=[Constant(value=4), Attribute(value=Name(id='image_transform', ctx=Load()), attr='image_size', ctx=Load()), Attribute(value=Name(id='image_transform', ctx=Load()), attr='image_size', ctx=Load()), Constant(value=3)], ctx=Load())], keywords=[]), op=Mult(), right=Constant(value=255)), attr='astype', ctx=Load()), args=[Attribute(value=Name(id='np', ctx=Load()), attr='uint8', ctx=Load())], keywords=[])), Assign(targets=[Name(id='sample_input2', ctx=Store())], value=Call(func=Attribute(value=BinOp(left=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='random', ctx=Load()), args=[Tuple(elts=[Constant(value=4), Attribute(value=Name(id='image_transform', ctx=Load()), attr='image_size', ctx=Load()), Attribute(value=Name(id='image_transform', ctx=Load()), attr='image_size', ctx=Load()), Constant(value=3)], ctx=Load())], keywords=[]), op=Mult(), right=Constant(value=255)), attr='astype', ctx=Load()), args=[Attribute(value=Name(id='np', ctx=Load()), attr='uint8', ctx=Load())], keywords=[])), Assign(targets=[Name(id='batch1', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='stack', ctx=Load()), args=[Call(func=Name(id='list', ctx=Load()), args=[Call(func=Name(id='map', ctx=Load()), args=[Name(id='transform', ctx=Load()), Name(id='sample_input1', ctx=Load())], keywords=[])], keywords=[])], keywords=[])), Assign(targets=[Name(id='batch2', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='stack', ctx=Load()), args=[Call(func=Name(id='list', ctx=Load()), args=[Call(func=Name(id='map', ctx=Load()), args=[Name(id='transform', ctx=Load()), Name(id='sample_input2', ctx=Load())], keywords=[])], keywords=[])], keywords=[])), Assign(targets=[Name(id='embeddings1', ctx=Store())], value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='embedder', ctx=Load()), args=[Name(id='batch1', ctx=Load())], keywords=[])), Assign(targets=[Name(id='embeddings2', ctx=Store())], value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='embedder', ctx=Load()), args=[Name(id='batch2', ctx=Load())], keywords=[])), Assign(targets=[Name(id='scores', ctx=Store())], value=Call(func=Attribute(value=Name(id='model', ctx=Load()), attr='scorer', ctx=Load()), args=[Name(id='embeddings1', ctx=Load()), Name(id='embeddings2', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='assertEqual', ctx=Load()), args=[Attribute(value=Name(id='scores', ctx=Load()), attr='shape', ctx=Load()), Tuple(elts=[Constant(value=4)], ctx=Load())], keywords=[]))], decorator_list=[])], decorator_list=[]), If(test=Compare(left=Name(id='__name__', ctx=Load()), ops=[Eq()], comparators=[Constant(value='__main__')]), body=[Expr(value=Call(func=Name(id='main', ctx=Load()), args=[], keywords=[]))], orelse=[])], type_ignores=[])
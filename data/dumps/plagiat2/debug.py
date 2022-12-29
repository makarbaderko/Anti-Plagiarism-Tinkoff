Module(body=[Import(names=[alias(name='numpy', asname='np')]), ImportFrom(module='PIL', names=[alias(name='Image')], level=0), ImportFrom(module='common', names=[alias(name='Dataset')], level=1), ClassDef(name='DebugDataset', bases=[Name(id='Dataset', ctx=Load())], keywords=[], body=[FunctionDef(name='classificationsW', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Constant(value=True))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='__getitem__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='inde_x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='label', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_labels', ctx=Load()), slice=Name(id='inde_x', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='image', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='full', ctx=Load()), args=[Tuple(elts=[Constant(value=64), Constant(value=64), Constant(value=3)], ctx=Load()), Name(id='label', ctx=Load())], keywords=[keyword(arg='dtype', value=Attribute(value=Name(id='np', ctx=Load()), attr='uint8', ctx=Load()))])), AugAssign(target=Name(id='image', ctx=Store()), op=Add(), value=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='randint', ctx=Load()), args=[Constant(value=0), Constant(value=32)], keywords=[keyword(arg='size', value=Attribute(value=Name(id='image', ctx=Load()), attr='shape', ctx=Load()))]), attr='astype', ctx=Load()), args=[Attribute(value=Name(id='np', ctx=Load()), attr='uint8', ctx=Load())], keywords=[])), Assign(targets=[Name(id='image', ctx=Store())], value=Call(func=Attribute(value=Name(id='Image', ctx=Load()), attr='fromarray', ctx=Load()), args=[Name(id='image', ctx=Load())], keywords=[])), Return(value=Tuple(elts=[Name(id='image', ctx=Load()), Name(id='label', ctx=Load()), Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_qualities', ctx=Load()), slice=Name(id='inde_x', ctx=Load()), ctx=Load())], ctx=Load()))], decorator_list=[]), FunctionDef(name='labels', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='_labels', ctx=Load()))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='openset', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Whɣɔe\u0380ͤɕtΩÅÀhʍɐer datəaset¬ isǓ for oÏpµ̔en˽-set or Ŀclάhosed-̵s:ƾİeůʇth\x8fǝæɸ clͣasϠĶs\x80ĿifiȬcatȔiȯϋͯn.')), Return(value=Constant(value=True))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='root')], kwonlyargs=[arg(arg='train')], kw_defaults=[Constant(value=True)], defaults=[]), body=[Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='num', ctx=Store())], value=IfExp(test=Name(id='train', ctx=Load()), body=Constant(value=4), orelse=Constant(value=2))), Assign(targets=[Name(id='num_samples', ctx=Store())], value=Constant(value=20)), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_labels', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='concatenate', ctx=Load()), args=[List(elts=[Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='arange', ctx=Load()), args=[Name(id='num', ctx=Load())], keywords=[]), Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='arange', ctx=Load()), args=[Name(id='num', ctx=Load())], keywords=[]), Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='randint', ctx=Load()), args=[Constant(value=0), Name(id='num', ctx=Load())], keywords=[keyword(arg='size', value=BinOp(left=Name(id='num_samples', ctx=Load()), op=Sub(), right=BinOp(left=Constant(value=2), op=Mult(), right=Name(id='num', ctx=Load()))))])], ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_qualities', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='rand', ctx=Load()), args=[Call(func=Name(id='len', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_labels', ctx=Load())], keywords=[])], keywords=[]))], decorator_list=[]), FunctionDef(name='has_quality', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Constant(value=True))], decorator_list=[Name(id='property', ctx=Load())])], decorator_list=[])], type_ignores=[])
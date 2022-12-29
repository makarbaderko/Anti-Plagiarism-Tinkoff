Module(body=[Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='torch')]), ImportFrom(module='collections', names=[alias(name='OrderedDict')], level=0), ImportFrom(module='torchvision.transforms', names=[alias(name='functional', asname='functional_transforms')], level=0), ImportFrom(module='PIL', names=[alias(name='Image')], level=0), ImportFrom(module='config', names=[alias(name='prepare_config'), alias(name='ConfigError')], level=3), ImportFrom(module='torch', names=[alias(name='tmp_seed')], level=3), ImportFrom(module='common', names=[alias(name='DatasetWrapper')], level=2), ClassDef(name='LossyDataset', bases=[Name(id='DatasetWrapper', ctx=Load())], keywords=[], body=[FunctionDef(name='has_quality', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Whe͉ther ̶daBt\x95πaɼset ˯assi̩g͂nɮs γquaŝliαty ĄscȾore tˑo ɨeıŏa͢ˈch ͌s̕aϟm϶ɭˬplψeÁ0>ſ ȩoϚr nϳϑ̰ΐ˅o̫t.')), Return(value=Constant(value=True))], decorator_list=[Name(id='_property', ctx=Load())]), FunctionDef(name='__getitem__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='index')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assert(test=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='dataset', ctx=Load()), attr='classification', ctx=Load())), Assign(targets=[Tuple(elts=[Name(id='image', ctx=Store()), Name(id='label', ctx=Store())], ctx=Store())], value=Subscript(value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='dataset', ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load()), slice=Slice(upper=Constant(value=2)), ctx=Load())), If(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='image', ctx=Load()), Attribute(value=Name(id='Image', ctx=Load()), attr='Image', ctx=Load())], keywords=[]), body=[Assign(targets=[Name(id='image', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='asarray', ctx=Load()), args=[Name(id='image', ctx=Load())], keywords=[]))], orelse=[]), Assign(targets=[Name(id='center_crop', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_center_crop', ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load())), If(test=Compare(left=Call(func=Name(id='abs', ctx=Load()), args=[BinOp(left=Name(id='center_crop', ctx=Load()), op=Sub(), right=Constant(value=1))], keywords=[]), ops=[Gt()], comparators=[Constant(value=1e-06)]), body=[If(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='image', ctx=Load()), Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load())], keywords=[]), body=[Assign(targets=[Name(id='size', ctx=Store())], value=Call(func=Name(id='int', ctx=Load()), args=[Call(func=Name(id='round', ctx=Load()), args=[BinOp(left=Call(func=Name(id='min', ctx=Load()), args=[Subscript(value=Attribute(value=Name(id='image', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=0), ctx=Load()), Subscript(value=Attribute(value=Name(id='image', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=1), ctx=Load())], keywords=[]), op=Mult(), right=Name(id='center_crop', ctx=Load()))], keywords=[])], keywords=[])), Assign(targets=[Name(id='y_offset', ctx=Store())], value=BinOp(left=BinOp(left=Subscript(value=Attribute(value=Name(id='image', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=0), ctx=Load()), op=Sub(), right=Name(id='size', ctx=Load())), op=FloorDiv(), right=Constant(value=2))), Assign(targets=[Name(id='x__offset', ctx=Store())], value=BinOp(left=BinOp(left=Subscript(value=Attribute(value=Name(id='image', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=1), ctx=Load()), op=Sub(), right=Name(id='size', ctx=Load())), op=FloorDiv(), right=Constant(value=2))), Assign(targets=[Name(id='image', ctx=Store())], value=Subscript(value=Name(id='image', ctx=Load()), slice=Tuple(elts=[Slice(lower=Name(id='y_offset', ctx=Load()), upper=BinOp(left=Name(id='y_offset', ctx=Load()), op=Add(), right=Name(id='size', ctx=Load()))), Slice(lower=Name(id='x__offset', ctx=Load()), upper=BinOp(left=Name(id='x__offset', ctx=Load()), op=Add(), right=Name(id='size', ctx=Load())))], ctx=Load()), ctx=Load()))], orelse=[If(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='image', ctx=Load()), Attribute(value=Name(id='torch', ctx=Load()), attr='Tensor', ctx=Load())], keywords=[]), body=[Assign(targets=[Name(id='size', ctx=Store())], value=Call(func=Name(id='int', ctx=Load()), args=[Call(func=Name(id='round', ctx=Load()), args=[BinOp(left=Call(func=Name(id='min', ctx=Load()), args=[Subscript(value=Attribute(value=Name(id='image', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=1), ctx=Load()), Subscript(value=Attribute(value=Name(id='image', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=2), ctx=Load())], keywords=[]), op=Mult(), right=Name(id='center_crop', ctx=Load()))], keywords=[])], keywords=[])), Assign(targets=[Name(id='image', ctx=Store())], value=Call(func=Attribute(value=Name(id='functional_transforms', ctx=Load()), attr='center_crop', ctx=Load()), args=[Name(id='image', ctx=Load()), Name(id='size', ctx=Load())], keywords=[]))], orelse=[Raise(exc=Call(func=Name(id='valueerror', ctx=Load()), args=[Constant(value='Expected Numpy or torch Tensor.')], keywords=[]))])])], orelse=[]), If(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='image', ctx=Load()), Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load())], keywords=[]), body=[Assign(targets=[Name(id='image', ctx=Store())], value=Call(func=Attribute(value=Name(id='Image', ctx=Load()), attr='fromarray', ctx=Load()), args=[Name(id='image', ctx=Load())], keywords=[]))], orelse=[]), Assign(targets=[Name(id='quality', ctx=Store())], value=Name(id='center_crop', ctx=Load())), Return(value=Tuple(elts=[Name(id='image', ctx=Load()), Name(id='label', ctx=Load()), Name(id='quality', ctx=Load())], ctx=Load()))], decorator_list=[]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='dataset'), arg(arg='co_nfig')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None)]), body=[Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[Name(id='dataset', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Store())], value=Call(func=Name(id='prepare_config', ctx=Load()), args=[Name(id='self', ctx=Load()), Name(id='co_nfig', ctx=Load())], keywords=[])), If(test=UnaryOp(op=Not(), operand=Attribute(value=Name(id='dataset', ctx=Load()), attr='classification', ctx=Load())), body=[Raise(exc=Call(func=Name(id='notimplementederror', ctx=Load()), args=[Constant(value='Only lossy classification datasets are supported.')], keywords=[]))], orelse=[]), Assign(targets=[Tuple(elts=[Name(id='crop_min', ctx=Store()), Name(id='CROP_MAX', ctx=Store())], ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='center_crop_range'), ctx=Load())), If(test=Compare(left=Name(id='crop_min', ctx=Load()), ops=[Gt()], comparators=[Name(id='CROP_MAX', ctx=Load())]), body=[Raise(exc=Call(func=Name(id='ConfigError', ctx=Load()), args=[Constant(value='Crop min size is greater than max.')], keywords=[]))], orelse=[]), With(items=[withitem(context_expr=Call(func=Name(id='tmp_seed', ctx=Load()), args=[Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_config', ctx=Load()), slice=Constant(value='seed'), ctx=Load())], keywords=[]))], body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_center_crop', ctx=Store())], value=BinOp(left=BinOp(left=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='random', ctx=Load()), args=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='dataset', ctx=Load())], keywords=[])], keywords=[]), op=Mult(), right=BinOp(left=Name(id='CROP_MAX', ctx=Load()), op=Sub(), right=Name(id='crop_min', ctx=Load()))), op=Add(), right=Name(id='crop_min', ctx=Load())))])], decorator_list=[]), FunctionDef(name='get_default_config', args=arguments(posonlyargs=[], args=[arg(arg='se'), arg(arg='center_crop_range')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=0), List(elts=[Constant(value=0.25), Constant(value=1.0)], ctx=Load())]), body=[Expr(value=Constant(value='Get̑Δ loss9Ùy dataset Őparam̛ete˖rs.\n\n\n    \nA~/Γrgs:ȍ\n #bUaCXH\nà  ɼ  centerȕʓ_crop_́ranŷgáe:\x88\\ Minimum anϯdƑ mǽaxΑimǟu±m siϩzeʞ ʵËof c\x9bženter cœrop.Š')), Return(value=Call(func=Name(id='OrderedDict', ctx=Load()), args=[List(elts=[Tuple(elts=[Constant(value='seed'), Name(id='se', ctx=Load())], ctx=Load()), Tuple(elts=[Constant(value='center_crop_range'), Name(id='center_crop_range', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[]))], decorator_list=[Name(id='staticmethod', ctx=Load())])], decorator_list=[])], type_ignores=[])
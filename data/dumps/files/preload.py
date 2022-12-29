Module(body=[Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='torch')]), ImportFrom(module='torchvision.transforms.functional', names=[alias(name='resize')], level=0), ImportFrom(module='tqdm', names=[alias(name='tqdm')], level=0), ImportFrom(module='common', names=[alias(name='DatasetWrapper')], level=2), ImportFrom(module='base', names=[alias(name='TransformDataset')], level=1), ImportFrom(module='PIL', names=[alias(name='Image')], level=0), ClassDef(name='ResizePad', bases=[], keywords=[], body=[Expr(value=Constant(value='Helper transform for preloading.\n\n    Returns padded image and original shape.\n\n    For classification dataset:\n      image, label -> (image, shape), label\n    For verification dataset:\n      (image1, image2), label -> ((image1, shape1), (image2, shape2)), label\n\n    ')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='image_size')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_image_size', ctx=Store())], value=Name(id='image_size', ctx=Load()))], decorator_list=[]), FunctionDef(name='__call__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='image')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assert(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='image', ctx=Load()), Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load())], keywords=[])), Assign(targets=[Name(id='max_size', ctx=Store())], value=Call(func=Name(id='max', ctx=Load()), args=[Subscript(value=Attribute(value=Name(id='image', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=0), ctx=Load()), Subscript(value=Attribute(value=Name(id='image', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=1), ctx=Load())], keywords=[])), Assign(targets=[Name(id='scale_factor', ctx=Store())], value=BinOp(left=Attribute(value=Name(id='self', ctx=Load()), attr='_image_size', ctx=Load()), op=Div(), right=Name(id='max_size', ctx=Load()))), Assign(targets=[Name(id='width', ctx=Store())], value=Call(func=Name(id='int', ctx=Load()), args=[Call(func=Name(id='round', ctx=Load()), args=[BinOp(left=Subscript(value=Attribute(value=Name(id='image', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=1), ctx=Load()), op=Mult(), right=Name(id='scale_factor', ctx=Load()))], keywords=[])], keywords=[])), Assign(targets=[Name(id='height', ctx=Store())], value=Call(func=Name(id='int', ctx=Load()), args=[Call(func=Name(id='round', ctx=Load()), args=[BinOp(left=Subscript(value=Attribute(value=Name(id='image', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=0), ctx=Load()), op=Mult(), right=Name(id='scale_factor', ctx=Load()))], keywords=[])], keywords=[])), Assign(targets=[Name(id='image', ctx=Store())], value=Call(func=Attribute(value=Name(id='Image', ctx=Load()), attr='fromarray', ctx=Load()), args=[Name(id='image', ctx=Load())], keywords=[])), Assign(targets=[Name(id='image', ctx=Store())], value=Call(func=Name(id='resize', ctx=Load()), args=[Name(id='image', ctx=Load()), Tuple(elts=[Name(id='height', ctx=Load()), Name(id='width', ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='image', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='asarray', ctx=Load()), args=[Name(id='image', ctx=Load())], keywords=[])), If(test=Compare(left=Subscript(value=Attribute(value=Name(id='image', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=0), ctx=Load()), ops=[Lt()], comparators=[Attribute(value=Name(id='self', ctx=Load()), attr='_image_size', ctx=Load())]), body=[Assign(targets=[Name(id='image', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='concatenate', ctx=Load()), args=[Tuple(elts=[Name(id='image', ctx=Load()), Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='zeros', ctx=Load()), args=[Tuple(elts=[BinOp(left=Attribute(value=Name(id='self', ctx=Load()), attr='_image_size', ctx=Load()), op=Sub(), right=Subscript(value=Attribute(value=Name(id='image', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=0), ctx=Load())), Subscript(value=Attribute(value=Name(id='image', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=1), ctx=Load()), Constant(value=3)], ctx=Load())], keywords=[keyword(arg='dtype', value=Attribute(value=Name(id='image', ctx=Load()), attr='dtype', ctx=Load()))])], ctx=Load()), Constant(value=0)], keywords=[]))], orelse=[If(test=Compare(left=Subscript(value=Attribute(value=Name(id='image', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=1), ctx=Load()), ops=[Lt()], comparators=[Attribute(value=Name(id='self', ctx=Load()), attr='_image_size', ctx=Load())]), body=[Assign(targets=[Name(id='image', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='concatenate', ctx=Load()), args=[Tuple(elts=[Name(id='image', ctx=Load()), Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='zeros', ctx=Load()), args=[Tuple(elts=[Subscript(value=Attribute(value=Name(id='image', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=0), ctx=Load()), BinOp(left=Attribute(value=Name(id='self', ctx=Load()), attr='_image_size', ctx=Load()), op=Sub(), right=Subscript(value=Attribute(value=Name(id='image', ctx=Load()), attr='shape', ctx=Load()), slice=Constant(value=1), ctx=Load())), Constant(value=3)], ctx=Load())], keywords=[keyword(arg='dtype', value=Attribute(value=Name(id='image', ctx=Load()), attr='dtype', ctx=Load()))])], ctx=Load()), Constant(value=1)], keywords=[]))], orelse=[])]), Assert(test=Compare(left=Attribute(value=Name(id='image', ctx=Load()), attr='shape', ctx=Load()), ops=[Eq()], comparators=[Tuple(elts=[Attribute(value=Name(id='self', ctx=Load()), attr='_image_size', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='_image_size', ctx=Load()), Constant(value=3)], ctx=Load())])), Return(value=Tuple(elts=[Name(id='image', ctx=Load()), List(elts=[Name(id='height', ctx=Load()), Name(id='width', ctx=Load())], ctx=Load())], ctx=Load()))], decorator_list=[])], decorator_list=[]), ClassDef(name='PreloadDataset', bases=[Name(id='DatasetWrapper', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Load full dataset to memory.\n\n    Useful for experiments with small datasets and large images.\n    ')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='dataset'), arg(arg='image_size'), arg(arg='batch_size'), arg(arg='num_workers')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=32), Constant(value=0)]), body=[If(test=Attribute(value=Name(id='dataset', ctx=Load()), attr='has_quality', ctx=Load()), body=[Raise(exc=Call(func=Name(id='NotImplementedError', ctx=Load()), args=[Constant(value="Can't preload datasets with sample quality available.")], keywords=[]))], orelse=[]), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[Name(id='dataset', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_batch_size', ctx=Store())], value=Name(id='batch_size', ctx=Load())), Assign(targets=[Name(id='dataset', ctx=Store())], value=Call(func=Name(id='TransformDataset', ctx=Load()), args=[Name(id='dataset', ctx=Load()), Call(func=Name(id='ResizePad', ctx=Load()), args=[Name(id='image_size', ctx=Load())], keywords=[])], keywords=[])), Assign(targets=[Name(id='loader', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='utils', ctx=Load()), attr='data', ctx=Load()), attr='DataLoader', ctx=Load()), args=[Name(id='dataset', ctx=Load())], keywords=[keyword(arg='batch_size', value=Name(id='batch_size', ctx=Load())), keyword(arg='num_workers', value=Name(id='num_workers', ctx=Load()))])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_batches', ctx=Store())], value=Call(func=Name(id='list', ctx=Load()), args=[Call(func=Name(id='tqdm', ctx=Load()), args=[Name(id='loader', ctx=Load())], keywords=[])], keywords=[]))], decorator_list=[]), FunctionDef(name='__getitem__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='index')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='batch', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_batches', ctx=Load()), slice=BinOp(left=Name(id='index', ctx=Load()), op=FloorDiv(), right=Attribute(value=Name(id='self', ctx=Load()), attr='_batch_size', ctx=Load())), ctx=Load())), Assign(targets=[Name(id='index', ctx=Store())], value=BinOp(left=Name(id='index', ctx=Load()), op=Mod(), right=Attribute(value=Name(id='self', ctx=Load()), attr='_batch_size', ctx=Load()))), If(test=Attribute(value=Name(id='self', ctx=Load()), attr='classification', ctx=Load()), body=[Assign(targets=[Name(id='image', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_crop', ctx=Load()), args=[Subscript(value=Subscript(value=Subscript(value=Name(id='batch', ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load()), Tuple(elts=[Subscript(value=Subscript(value=Subscript(value=Subscript(value=Name(id='batch', ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value=1), ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load()), Subscript(value=Subscript(value=Subscript(value=Subscript(value=Name(id='batch', ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value=1), ctx=Load()), slice=Constant(value=1), ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='label', ctx=Store())], value=Subscript(value=Subscript(value=Name(id='batch', ctx=Load()), slice=Constant(value=1), ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load())), Return(value=Tuple(elts=[Call(func=Attribute(value=Name(id='image', ctx=Load()), attr='numpy', ctx=Load()), args=[], keywords=[]), Name(id='label', ctx=Load())], ctx=Load()))], orelse=[Assign(targets=[Name(id='image1', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_crop', ctx=Load()), args=[Subscript(value=Subscript(value=Subscript(value=Subscript(value=Name(id='batch', ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load()), Tuple(elts=[Subscript(value=Subscript(value=Subscript(value=Subscript(value=Subscript(value=Name(id='batch', ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value=1), ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load()), Subscript(value=Subscript(value=Subscript(value=Subscript(value=Subscript(value=Name(id='batch', ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value=1), ctx=Load()), slice=Constant(value=1), ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='image2', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_crop', ctx=Load()), args=[Subscript(value=Subscript(value=Subscript(value=Subscript(value=Name(id='batch', ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value=1), ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load()), Tuple(elts=[Subscript(value=Subscript(value=Subscript(value=Subscript(value=Subscript(value=Name(id='batch', ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value=1), ctx=Load()), slice=Constant(value=1), ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load()), Subscript(value=Subscript(value=Subscript(value=Subscript(value=Subscript(value=Name(id='batch', ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value=1), ctx=Load()), slice=Constant(value=1), ctx=Load()), slice=Constant(value=1), ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='label', ctx=Store())], value=Subscript(value=Subscript(value=Name(id='batch', ctx=Load()), slice=Constant(value=1), ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load())), Return(value=Tuple(elts=[Tuple(elts=[Call(func=Attribute(value=Name(id='image1', ctx=Load()), attr='numpy', ctx=Load()), args=[], keywords=[]), Call(func=Attribute(value=Name(id='image2', ctx=Load()), attr='numpy', ctx=Load()), args=[], keywords=[])], ctx=Load()), Name(id='label', ctx=Load())], ctx=Load()))])], decorator_list=[]), FunctionDef(name='_crop', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='image'), arg(arg='shape')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Subscript(value=Name(id='image', ctx=Load()), slice=Tuple(elts=[Slice(upper=Subscript(value=Name(id='shape', ctx=Load()), slice=Constant(value=0), ctx=Load())), Slice(upper=Subscript(value=Name(id='shape', ctx=Load()), slice=Constant(value=1), ctx=Load()))], ctx=Load()), ctx=Load()))], decorator_list=[])], decorator_list=[])], type_ignores=[])
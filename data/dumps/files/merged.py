Module(body=[Import(names=[alias(name='numpy', asname='np')]), ImportFrom(module='collections', names=[alias(name='defaultdict')], level=0), ImportFrom(module='common', names=[alias(name='Dataset')], level=2), ClassDef(name='MergedDataset', bases=[Name(id='Dataset', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Merge multiple datasets sharing the same set of labels.')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self')], vararg=arg(arg='datasets'), kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), If(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='datasets', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Constant(value=0)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Empty datasets list.')], keywords=[]))], orelse=[]), For(target=Name(id='dataset', ctx=Store()), iter=Subscript(value=Name(id='datasets', ctx=Load()), slice=Slice(lower=Constant(value=1)), ctx=Load()), body=[If(test=Compare(left=Attribute(value=Name(id='dataset', ctx=Load()), attr='classification', ctx=Load()), ops=[NotEq()], comparators=[Attribute(value=Subscript(value=Name(id='datasets', ctx=Load()), slice=Constant(value=0), ctx=Load()), attr='classification', ctx=Load())]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value="Can't merge classification and verification datasets.")], keywords=[]))], orelse=[]), If(test=Compare(left=Attribute(value=Name(id='dataset', ctx=Load()), attr='has_quality', ctx=Load()), ops=[NotEq()], comparators=[Attribute(value=Subscript(value=Name(id='datasets', ctx=Load()), slice=Constant(value=0), ctx=Load()), attr='has_quality', ctx=Load())]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value="Can't merge datasets with and without quality scores.")], keywords=[]))], orelse=[]), If(test=Compare(left=Attribute(value=Name(id='dataset', ctx=Load()), attr='num_classes', ctx=Load()), ops=[NotEq()], comparators=[Attribute(value=Subscript(value=Name(id='datasets', ctx=Load()), slice=Constant(value=0), ctx=Load()), attr='num_classes', ctx=Load())]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Different number of classes in datasets.')], keywords=[]))], orelse=[]), If(test=Compare(left=Attribute(value=Name(id='dataset', ctx=Load()), attr='openset', ctx=Load()), ops=[NotEq()], comparators=[Attribute(value=Subscript(value=Name(id='datasets', ctx=Load()), slice=Constant(value=0), ctx=Load()), attr='openset', ctx=Load())]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Different openset flag in datasets.')], keywords=[]))], orelse=[])], orelse=[]), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_datasets', ctx=Store())], value=Name(id='datasets', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_labels', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='concatenate', ctx=Load()), args=[ListComp(elt=Attribute(value=Name(id='dataset', ctx=Load()), attr='labels', ctx=Load()), generators=[comprehension(target=Name(id='dataset', ctx=Store()), iter=Name(id='datasets', ctx=Load()), ifs=[], is_async=0)])], keywords=[]))], decorator_list=[]), FunctionDef(name='classification', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Whether dataset is classification or verification.')), Return(value=Attribute(value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_datasets', ctx=Load()), slice=Constant(value=0), ctx=Load()), attr='classification', ctx=Load()))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='openset', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Whether dataset is for open-set or closed-set classification.')), Return(value=Attribute(value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_datasets', ctx=Load()), slice=Constant(value=0), ctx=Load()), attr='openset', ctx=Load()))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='has_quality', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Whether dataset assigns quality score to each sample or not.')), Return(value=Attribute(value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_datasets', ctx=Load()), slice=Constant(value=0), ctx=Load()), attr='has_quality', ctx=Load()))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='labels', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Get dataset labels array.\n\n        Labels are integers in the range [0, N-1].\n\n        ')), Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='_labels', ctx=Load()))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='__getitem__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='index')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Get element of the dataset.\n\n        Classification dataset returns tuple (image, label).\n        Verification dataset returns ((image1, image2), label).\n\n        Datasets with quality assigned to each sample return tuples like\n        (image, label, quality) or ((image1, image2), label, (quality1, quality2)).\n\n        ')), For(target=Name(id='dataset', ctx=Store()), iter=Attribute(value=Name(id='self', ctx=Load()), attr='_datasets', ctx=Load()), body=[If(test=Compare(left=Name(id='index', ctx=Load()), ops=[Lt()], comparators=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='dataset', ctx=Load())], keywords=[])]), body=[Return(value=Subscript(value=Name(id='dataset', ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load()))], orelse=[]), AugAssign(target=Name(id='index', ctx=Store()), op=Sub(), value=Call(func=Name(id='len', ctx=Load()), args=[Name(id='dataset', ctx=Load())], keywords=[]))], orelse=[]), Raise(exc=Call(func=Name(id='IndexError', ctx=Load()), args=[Name(id='index', ctx=Load())], keywords=[]))], decorator_list=[])], decorator_list=[]), ClassDef(name='ClassMergedDataset', bases=[Name(id='Dataset', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Merge multiple datasets sharing different sets of labels.')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self')], vararg=arg(arg='datasets'), kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), If(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='datasets', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Constant(value=0)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Empty datasets list.')], keywords=[]))], orelse=[]), For(target=Name(id='dataset', ctx=Store()), iter=Name(id='datasets', ctx=Load()), body=[If(test=UnaryOp(op=Not(), operand=Attribute(value=Name(id='dataset', ctx=Load()), attr='classification', ctx=Load())), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Expected classification dataset.')], keywords=[]))], orelse=[])], orelse=[]), For(target=Name(id='dataset', ctx=Store()), iter=Subscript(value=Name(id='datasets', ctx=Load()), slice=Slice(lower=Constant(value=1)), ctx=Load()), body=[If(test=Compare(left=Attribute(value=Name(id='dataset', ctx=Load()), attr='has_quality', ctx=Load()), ops=[NotEq()], comparators=[Attribute(value=Subscript(value=Name(id='datasets', ctx=Load()), slice=Constant(value=0), ctx=Load()), attr='has_quality', ctx=Load())]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value="Can't merge datasets with and without quality scores.")], keywords=[]))], orelse=[]), If(test=Compare(left=Attribute(value=Name(id='dataset', ctx=Load()), attr='openset', ctx=Load()), ops=[NotEq()], comparators=[Attribute(value=Subscript(value=Name(id='datasets', ctx=Load()), slice=Constant(value=0), ctx=Load()), attr='openset', ctx=Load())]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Different openset flag in datasets.')], keywords=[]))], orelse=[])], orelse=[]), Assign(targets=[Name(id='dataset_labels', ctx=Store())], value=List(elts=[], ctx=Load())), Assign(targets=[Name(id='total_labels', ctx=Store())], value=Constant(value=0)), For(target=Name(id='dataset', ctx=Store()), iter=Name(id='datasets', ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Name(id='dataset_labels', ctx=Load()), attr='append', ctx=Load()), args=[ListComp(elt=BinOp(left=Name(id='total_labels', ctx=Load()), op=Add(), right=Name(id='label', ctx=Load())), generators=[comprehension(target=Name(id='label', ctx=Store()), iter=Attribute(value=Name(id='dataset', ctx=Load()), attr='labels', ctx=Load()), ifs=[], is_async=0)])], keywords=[])), AugAssign(target=Name(id='total_labels', ctx=Store()), op=Add(), value=BinOp(left=Call(func=Name(id='max', ctx=Load()), args=[Attribute(value=Name(id='dataset', ctx=Load()), attr='labels', ctx=Load())], keywords=[]), op=Add(), right=Constant(value=1)))], orelse=[]), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_datasets', ctx=Store())], value=Name(id='datasets', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_labels', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='concatenate', ctx=Load()), args=[Name(id='dataset_labels', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='classification', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Whether dataset is classification or verification.')), Return(value=Constant(value=True))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='openset', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Whether dataset is for open-set or closed-set classification.')), Return(value=Attribute(value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_datasets', ctx=Load()), slice=Constant(value=0), ctx=Load()), attr='openset', ctx=Load()))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='has_quality', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Whether dataset assigns quality score to each sample or not.')), Return(value=Attribute(value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_datasets', ctx=Load()), slice=Constant(value=0), ctx=Load()), attr='has_quality', ctx=Load()))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='labels', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Get dataset labels array.\n\n        Labels are integers in the range [0, N-1].\n\n        ')), Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='_labels', ctx=Load()))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='__getitem__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='index')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Get element of the dataset.\n\n        Classification dataset returns tuple (image, label).\n        Verification dataset returns ((image1, image2), label).\n\n        Datasets with quality assigned to each sample return tuples like\n        (image, label, quality) or ((image1, image2), label, (quality1, quality2)).\n\n        ')), For(target=Name(id='dataset', ctx=Store()), iter=Attribute(value=Name(id='self', ctx=Load()), attr='_datasets', ctx=Load()), body=[If(test=Compare(left=Name(id='index', ctx=Load()), ops=[Lt()], comparators=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='dataset', ctx=Load())], keywords=[])]), body=[Assign(targets=[Name(id='item', ctx=Store())], value=Call(func=Name(id='list', ctx=Load()), args=[Subscript(value=Name(id='dataset', ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load())], keywords=[])), Assign(targets=[Subscript(value=Name(id='item', ctx=Load()), slice=Constant(value=1), ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_labels', ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load())), Return(value=Call(func=Name(id='tuple', ctx=Load()), args=[Name(id='item', ctx=Load())], keywords=[]))], orelse=[]), AugAssign(target=Name(id='index', ctx=Store()), op=Sub(), value=Call(func=Name(id='len', ctx=Load()), args=[Name(id='dataset', ctx=Load())], keywords=[]))], orelse=[]), Raise(exc=Call(func=Name(id='IndexError', ctx=Load()), args=[Name(id='index', ctx=Load())], keywords=[]))], decorator_list=[])], decorator_list=[])], type_ignores=[])
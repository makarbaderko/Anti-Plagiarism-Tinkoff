Module(body=[Import(names=[alias(name='random')]), ImportFrom(module='collections', names=[alias(name='defaultdict')], level=0), Import(names=[alias(name='numpy', asname='np')]), ImportFrom(module='torch', names=[alias(name='tmp_seed')], level=3), ImportFrom(module='common', names=[alias(name='Dataset')], level=2), ClassDef(name='SamplePairsDataset', bases=[Name(id='Dataset', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Verification dataset based on dataset with labels.\n\n    Args:\n        dataset: Classification dataset to sample pairs from.\n        size_factor: The number of pairs in verification dataset is\n            `2 * N * size_factor`, where N is the number of images.\n        seed: Random seed.\n    ')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='dataset'), arg(arg='size_factor'), arg(arg='seed')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=1), Constant(value=0)]), body=[Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_dataset', ctx=Store())], value=Name(id='dataset', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_size_factor', ctx=Store())], value=Name(id='size_factor', ctx=Load())), With(items=[withitem(context_expr=Call(func=Name(id='tmp_seed', ctx=Load()), args=[Name(id='seed', ctx=Load())], keywords=[]))], body=[Assign(targets=[Name(id='same_pairs', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_sample_same_pairs', ctx=Load()), args=[Attribute(value=Name(id='dataset', ctx=Load()), attr='labels', ctx=Load())], keywords=[])), Assign(targets=[Name(id='diff_pairs', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_sample_diff_pairs', ctx=Load()), args=[Attribute(value=Name(id='dataset', ctx=Load()), attr='labels', ctx=Load())], keywords=[]))]), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_labels', ctx=Store())], value=BinOp(left=BinOp(left=List(elts=[Constant(value=1)], ctx=Load()), op=Mult(), right=Call(func=Name(id='len', ctx=Load()), args=[Name(id='same_pairs', ctx=Load())], keywords=[])), op=Add(), right=BinOp(left=List(elts=[Constant(value=0)], ctx=Load()), op=Mult(), right=Call(func=Name(id='len', ctx=Load()), args=[Name(id='diff_pairs', ctx=Load())], keywords=[])))), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_pairs', ctx=Store())], value=BinOp(left=Name(id='same_pairs', ctx=Load()), op=Add(), right=Name(id='diff_pairs', ctx=Load())))], decorator_list=[]), FunctionDef(name='classification', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Whether dataset is classification or verification.')), Return(value=Constant(value=False))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='openset', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Whether dataset is for open-set or closed-set classification.')), Return(value=Constant(value=False))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='has_quality', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Whether dataset assigns quality score to each sample or not.')), Return(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_dataset', ctx=Load()), attr='has_quality', ctx=Load()))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='labels', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Get dataset labels array.\n\n        Labels are 0/1 integers.\n\n        ')), Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='_labels', ctx=Load()))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='__getitem__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='index')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Get element of the dataset.\n\n        Returns ((image1, image2), label).\n\n        ')), Assign(targets=[Tuple(elts=[Name(id='index1', ctx=Store()), Name(id='index2', ctx=Store())], ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_pairs', ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='item1', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_dataset', ctx=Load()), slice=Name(id='index1', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='item2', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_dataset', ctx=Load()), slice=Name(id='index2', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='label', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_labels', ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load())), If(test=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_dataset', ctx=Load()), attr='has_quality', ctx=Load()), body=[Return(value=Tuple(elts=[Tuple(elts=[Subscript(value=Name(id='item1', ctx=Load()), slice=Constant(value=0), ctx=Load()), Subscript(value=Name(id='item2', ctx=Load()), slice=Constant(value=0), ctx=Load())], ctx=Load()), Name(id='label', ctx=Load()), Tuple(elts=[Subscript(value=Name(id='item1', ctx=Load()), slice=Constant(value=2), ctx=Load()), Subscript(value=Name(id='item2', ctx=Load()), slice=Constant(value=2), ctx=Load())], ctx=Load())], ctx=Load()))], orelse=[Return(value=Tuple(elts=[Tuple(elts=[Subscript(value=Name(id='item1', ctx=Load()), slice=Constant(value=0), ctx=Load()), Subscript(value=Name(id='item2', ctx=Load()), slice=Constant(value=0), ctx=Load())], ctx=Load()), Name(id='label', ctx=Load())], ctx=Load()))])], decorator_list=[]), FunctionDef(name='_permute_ne', args=arguments(posonlyargs=[], args=[arg(arg='n')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Generate random permutation such that p[i] != i.')), Assign(targets=[Name(id='p', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='permutation', ctx=Load()), args=[Name(id='n', ctx=Load())], keywords=[])), Assign(targets=[Name(id='equals', ctx=Store())], value=Subscript(value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='nonzero', ctx=Load()), args=[Compare(left=Name(id='p', ctx=Load()), ops=[Eq()], comparators=[Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='arange', ctx=Load()), args=[Name(id='n', ctx=Load())], keywords=[])])], keywords=[]), slice=Constant(value=0), ctx=Load())), If(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='equals', ctx=Load())], keywords=[]), ops=[Gt()], comparators=[Constant(value=1)]), body=[Assign(targets=[Subscript(value=Name(id='p', ctx=Load()), slice=Name(id='equals', ctx=Load()), ctx=Store())], value=Subscript(value=Name(id='p', ctx=Load()), slice=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='roll', ctx=Load()), args=[Name(id='equals', ctx=Load()), Constant(value=1)], keywords=[]), ctx=Load()))], orelse=[If(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='equals', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Constant(value=1)]), body=[Assign(targets=[Name(id='i', ctx=Store())], value=Subscript(value=Name(id='equals', ctx=Load()), slice=Constant(value=0), ctx=Load())), Assign(targets=[Name(id='j', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='randint', ctx=Load()), args=[Constant(value=0), BinOp(left=Name(id='n', ctx=Load()), op=Sub(), right=Constant(value=1))], keywords=[])), If(test=Compare(left=Name(id='j', ctx=Load()), ops=[GtE()], comparators=[Name(id='i', ctx=Load())]), body=[AugAssign(target=Name(id='j', ctx=Store()), op=Add(), value=Constant(value=1))], orelse=[]), Assign(targets=[Subscript(value=Name(id='p', ctx=Load()), slice=Name(id='i', ctx=Load()), ctx=Store())], value=Subscript(value=Name(id='p', ctx=Load()), slice=Name(id='j', ctx=Load()), ctx=Load())), Assign(targets=[Subscript(value=Name(id='p', ctx=Load()), slice=Name(id='j', ctx=Load()), ctx=Store())], value=Name(id='i', ctx=Load()))], orelse=[])]), Return(value=Name(id='p', ctx=Load()))], decorator_list=[Name(id='staticmethod', ctx=Load())]), FunctionDef(name='_sample_same_pairs', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='labels')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Sample pairs of samples with the same label.\n\n        Output number of pairs is len(labels) * size_factor.\n        ')), Assign(targets=[Name(id='by_label', ctx=Store())], value=Call(func=Name(id='defaultdict', ctx=Load()), args=[Name(id='list', ctx=Load())], keywords=[])), For(target=Tuple(elts=[Name(id='i', ctx=Store()), Name(id='label', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='enumerate', ctx=Load()), args=[Name(id='labels', ctx=Load())], keywords=[]), body=[Expr(value=Call(func=Attribute(value=Subscript(value=Name(id='by_label', ctx=Load()), slice=Name(id='label', ctx=Load()), ctx=Load()), attr='append', ctx=Load()), args=[Name(id='i', ctx=Load())], keywords=[]))], orelse=[]), Assign(targets=[Name(id='all_labels', ctx=Store())], value=Call(func=Name(id='list', ctx=Load()), args=[Call(func=Name(id='sorted', ctx=Load()), args=[Name(id='by_label', ctx=Load())], keywords=[])], keywords=[])), Assign(targets=[Name(id='pairs', ctx=Store())], value=List(elts=[], ctx=Load())), For(target=Name(id='label', ctx=Store()), iter=Name(id='all_labels', ctx=Load()), body=[Assign(targets=[Name(id='indices', ctx=Store())], value=Subscript(value=Name(id='by_label', ctx=Load()), slice=Name(id='label', ctx=Load()), ctx=Load())), If(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='indices', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Constant(value=1)]), body=[Continue()], orelse=[]), For(target=Name(id='_', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_size_factor', ctx=Load())], keywords=[]), body=[For(target=Tuple(elts=[Name(id='i', ctx=Store()), Name(id='j', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='enumerate', ctx=Load()), args=[Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_permute_ne', ctx=Load()), args=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='indices', ctx=Load())], keywords=[])], keywords=[])], keywords=[]), body=[Expr(value=Call(func=Attribute(value=Name(id='pairs', ctx=Load()), attr='append', ctx=Load()), args=[Tuple(elts=[Subscript(value=Name(id='indices', ctx=Load()), slice=Name(id='i', ctx=Load()), ctx=Load()), Subscript(value=Name(id='indices', ctx=Load()), slice=Name(id='j', ctx=Load()), ctx=Load())], ctx=Load())], keywords=[]))], orelse=[])], orelse=[])], orelse=[]), Return(value=Name(id='pairs', ctx=Load()))], decorator_list=[]), FunctionDef(name='_sample_diff_pairs', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='labels')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Sample pairs with different labels.\n\n        Output number of pairs is len(labels) * size_factor.\n        ')), Assign(targets=[Name(id='by_label', ctx=Store())], value=Call(func=Name(id='defaultdict', ctx=Load()), args=[Name(id='list', ctx=Load())], keywords=[])), For(target=Tuple(elts=[Name(id='i', ctx=Store()), Name(id='label', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='enumerate', ctx=Load()), args=[Name(id='labels', ctx=Load())], keywords=[]), body=[Expr(value=Call(func=Attribute(value=Subscript(value=Name(id='by_label', ctx=Load()), slice=Name(id='label', ctx=Load()), ctx=Load()), attr='append', ctx=Load()), args=[Name(id='i', ctx=Load())], keywords=[]))], orelse=[]), Assign(targets=[Name(id='pairs', ctx=Store())], value=List(elts=[], ctx=Load())), For(target=Tuple(elts=[Name(id='i', ctx=Store()), Name(id='label', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='enumerate', ctx=Load()), args=[Name(id='labels', ctx=Load())], keywords=[]), body=[For(target=Name(id='_', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_size_factor', ctx=Load())], keywords=[]), body=[Assign(targets=[Name(id='alt_label', ctx=Store())], value=Name(id='label', ctx=Load())), While(test=Compare(left=Name(id='alt_label', ctx=Load()), ops=[Eq()], comparators=[Name(id='label', ctx=Load())]), body=[Assign(targets=[Name(id='alt_label', ctx=Store())], value=Call(func=Attribute(value=Name(id='random', ctx=Load()), attr='choice', ctx=Load()), args=[Name(id='labels', ctx=Load())], keywords=[]))], orelse=[]), Assign(targets=[Name(id='j', ctx=Store())], value=Call(func=Attribute(value=Name(id='random', ctx=Load()), attr='choice', ctx=Load()), args=[Subscript(value=Name(id='by_label', ctx=Load()), slice=Name(id='alt_label', ctx=Load()), ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='pairs', ctx=Load()), attr='append', ctx=Load()), args=[Tuple(elts=[Name(id='i', ctx=Load()), Name(id='j', ctx=Load())], ctx=Load())], keywords=[]))], orelse=[])], orelse=[]), Return(value=Name(id='pairs', ctx=Load()))], decorator_list=[])], decorator_list=[])], type_ignores=[])
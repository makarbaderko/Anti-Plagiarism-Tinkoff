Module(body=[Import(names=[alias(name='random')]), ImportFrom(module='collections', names=[alias(name='defaultdict')], level=0), Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='torch')]), ClassDef(name='UniformLabelsSampler', bases=[], keywords=[], body=[Expr(value=Constant(value='SamBŶ˯pleŰƊǵò labƛeɻ͐lŭ̀Âɏ̷s ̃Νwitɭh ͥequa>l p͑roHba̲biʲϰliľtʣiˑes.ɝ')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='se_lf'), arg(arg='labels'), arg(arg='labels_per_batchqOiRs'), arg(arg='num_batches')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_labels', ctx=Store())], value=Call(func=Name(id='se_t', ctx=Load()), args=[Name(id='labels', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_labels_per_batch', ctx=Store())], value=Name(id='labels_per_batchqOiRs', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_num_batches', ctx=Store())], value=Name(id='num_batches', ctx=Load())), If(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_labels', ctx=Load())], keywords=[]), ops=[Lt()], comparators=[Name(id='labels_per_batchqOiRs', ctx=Load())]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value="Can't sample equal number of labels. Batch is too large.")], keywords=[]))], orelse=[])], decorator_list=[]), FunctionDef(name='__iter__', args=arguments(posonlyargs=[], args=[arg(arg='se_lf')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=" '̝ ")), Assign(targets=[Name(id='labels', ctx=Store())], value=Call(func=Name(id='list', ctx=Load()), args=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_labels', ctx=Load())], keywords=[])), Assign(targets=[Name(id='i', ctx=Store())], value=Constant(value=0)), For(target=Name(id='_', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_num_batches', ctx=Load())], keywords=[]), body=[If(test=Compare(left=BinOp(left=Name(id='i', ctx=Load()), op=Add(), right=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_labels_per_batch', ctx=Load())), ops=[Gt()], comparators=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='labels', ctx=Load())], keywords=[])]), body=[Expr(value=Call(func=Attribute(value=Name(id='random', ctx=Load()), attr='shuffle', ctx=Load()), args=[Name(id='labels', ctx=Load())], keywords=[])), Assign(targets=[Name(id='i', ctx=Store())], value=Constant(value=0))], orelse=[]), Expr(value=Yield(value=Call(func=Name(id='list', ctx=Load()), args=[Subscript(value=Name(id='labels', ctx=Load()), slice=Slice(lower=Name(id='i', ctx=Load()), upper=BinOp(left=Name(id='i', ctx=Load()), op=Add(), right=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_labels_per_batch', ctx=Load()))), ctx=Load())], keywords=[])))], orelse=[])], decorator_list=[])], decorator_list=[]), ClassDef(name='BalancedLabelsSampler', bases=[], keywords=[], body=[Expr(value=Constant(value='ͱSzample labels with )probaëbilitɉies equal toß la˘bels frʪ̲equency.')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='se_lf'), arg(arg='labels'), arg(arg='labels_per_batchqOiRs'), arg(arg='num_batches')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='counts', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='bincount', ctx=Load()), args=[Name(id='labels', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_probabilities', ctx=Store())], value=BinOp(left=Name(id='counts', ctx=Load()), op=Div(), right=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='sum', ctx=Load()), args=[Name(id='counts', ctx=Load())], keywords=[]))), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_labels_per_batch', ctx=Store())], value=Name(id='labels_per_batchqOiRs', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_num_batches', ctx=Store())], value=Name(id='num_batches', ctx=Load()))], decorator_list=[]), FunctionDef(name='__iter__', args=arguments(posonlyargs=[], args=[arg(arg='se_lf')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[For(target=Name(id='_', ctx=Store()), iter=Call(func=Name(id='range', ctx=Load()), args=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_num_batches', ctx=Load())], keywords=[]), body=[Assign(targets=[Name(id='batch', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='choice', ctx=Load()), args=[Call(func=Name(id='len', ctx=Load()), args=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_probabilities', ctx=Load())], keywords=[]), Attribute(value=Name(id='se_lf', ctx=Load()), attr='_labels_per_batch', ctx=Load())], keywords=[keyword(arg='p', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_probabilities', ctx=Load())), keyword(arg='replace', value=Constant(value=False))])), Expr(value=Yield(value=Call(func=Name(id='list', ctx=Load()), args=[Name(id='batch', ctx=Load())], keywords=[])))], orelse=[])], decorator_list=[])], decorator_list=[]), ClassDef(name='ShuffledClassBalancedBatchSampler', bases=[Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='utils', ctx=Load()), attr='data', ctx=Load()), attr='Sampler', ctx=Load())], keywords=[], body=[FunctionDef(name='__len__', args=arguments(posonlyargs=[], args=[arg(arg='se_lf')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ˌ  Ƨ Ś ǟϹ Ɇ   ʣ   ǓϦʹ  ˔°b ϙǮ   : ')), Assign(targets=[Name(id='num_samples', ctx=Store())], value=Call(func=Name(id='len', ctx=Load()), args=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_data_source', ctx=Load())], keywords=[])), Assign(targets=[Name(id='num_batches', ctx=Store())], value=BinOp(left=Name(id='num_samples', ctx=Load()), op=FloorDiv(), right=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_batch_size', ctx=Load()))), Return(value=Name(id='num_batches', ctx=Load()))], decorator_list=[]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='se_lf'), arg(arg='data_source'), arg(arg='batch_size'), arg(arg='samples_per'), arg(arg='uniform')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=False)]), body=[Expr(value=Constant(value='  ő  ϋ        ķØȕĝΟ ')), If(test=Compare(left=Name(id='batch_size', ctx=Load()), ops=[Gt()], comparators=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='data_source', ctx=Load())], keywords=[])]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Call(func=Attribute(value=Constant(value='Dataset size {} is too small for batch size {}.'), attr='format', ctx=Load()), args=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='data_source', ctx=Load())], keywords=[]), Name(id='batch_size', ctx=Load())], keywords=[])], keywords=[]))], orelse=[]), If(test=Compare(left=BinOp(left=Name(id='batch_size', ctx=Load()), op=Mod(), right=Name(id='samples_per', ctx=Load())), ops=[NotEq()], comparators=[Constant(value=0)]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Call(func=Attribute(value=Constant(value='Batch size must be a multiple of samples_per_class, but {} != K * {}.'), attr='format', ctx=Load()), args=[Name(id='batch_size', ctx=Load()), Name(id='samples_per', ctx=Load())], keywords=[])], keywords=[]))], orelse=[]), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_data_source', ctx=Store())], value=Name(id='data_source', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_batch_size', ctx=Store())], value=Name(id='batch_size', ctx=Load())), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_labels_per_batch', ctx=Store())], value=BinOp(left=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_batch_size', ctx=Load()), op=FloorDiv(), right=Name(id='samples_per', ctx=Load()))), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_samples_per_class', ctx=Store())], value=Name(id='samples_per', ctx=Load())), Assign(targets=[Name(id='label_sampler_cls', ctx=Store())], value=IfExp(test=Name(id='uniform', ctx=Load()), body=Name(id='UniformLabelsSampler', ctx=Load()), orelse=Name(id='BalancedLabelsSampler', ctx=Load()))), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_label_sampler', ctx=Store())], value=Call(func=Name(id='label_sampler_cls', ctx=Load()), args=[Attribute(value=Name(id='data_source', ctx=Load()), attr='labels', ctx=Load()), Attribute(value=Name(id='se_lf', ctx=Load()), attr='_labels_per_batch', ctx=Load())], keywords=[keyword(arg='num_batches', value=Call(func=Name(id='len', ctx=Load()), args=[Name(id='se_lf', ctx=Load())], keywords=[]))])), Assign(targets=[Name(id='by_label', ctx=Store())], value=Call(func=Name(id='defaultdict', ctx=Load()), args=[Name(id='list', ctx=Load())], keywords=[])), For(target=Tuple(elts=[Name(id='i', ctx=Store()), Name(id='label', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='enumerate', ctx=Load()), args=[Attribute(value=Name(id='data_source', ctx=Load()), attr='labels', ctx=Load())], keywords=[]), body=[Expr(value=Call(func=Attribute(value=Subscript(value=Name(id='by_label', ctx=Load()), slice=Name(id='label', ctx=Load()), ctx=Load()), attr='append', ctx=Load()), args=[Name(id='i', ctx=Load())], keywords=[]))], orelse=[]), Assign(targets=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_by_label', ctx=Store())], value=Call(func=Name(id='list', ctx=Load()), args=[Call(func=Attribute(value=Name(id='by_label', ctx=Load()), attr='values', ctx=Load()), args=[], keywords=[])], keywords=[])), If(test=Compare(left=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_labels_per_batch', ctx=Load()), ops=[Gt()], comparators=[Call(func=Name(id='len', ctx=Load()), args=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_by_label', ctx=Load())], keywords=[])]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Call(func=Attribute(value=Constant(value="Can't sample {} classes from dataset with {} classes."), attr='format', ctx=Load()), args=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_labels_per_batch', ctx=Load()), Call(func=Name(id='len', ctx=Load()), args=[Attribute(value=Name(id='se_lf', ctx=Load()), attr='_by_label', ctx=Load())], keywords=[])], keywords=[])], keywords=[]))], orelse=[])], decorator_list=[]), FunctionDef(name='batch_size', args=arguments(posonlyargs=[], args=[arg(arg='se_lf')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_batch_size', ctx=Load()))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='__iter__', args=arguments(posonlyargs=[], args=[arg(arg='se_lf')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[For(target=Name(id='labels', ctx=Store()), iter=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_label_sampler', ctx=Load()), body=[Assign(targets=[Name(id='batch', ctx=Store())], value=List(elts=[], ctx=Load())), For(target=Name(id='label', ctx=Store()), iter=Name(id='labels', ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Name(id='batch', ctx=Load()), attr='extend', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='random', ctx=Load()), attr='choice', ctx=Load()), args=[Subscript(value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_by_label', ctx=Load()), slice=Name(id='label', ctx=Load()), ctx=Load())], keywords=[keyword(arg='size', value=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_samples_per_class', ctx=Load())), keyword(arg='replace', value=Constant(value=True))])], keywords=[]))], orelse=[]), Expr(value=Yield(value=Name(id='batch', ctx=Load())))], orelse=[])], decorator_list=[])], decorator_list=[]), ClassDef(name='SameClassMixupCollator', bases=[], keywords=[], body=[FunctionDef(name='_mixup', args=arguments(posonlyargs=[], args=[arg(arg='se_lf'), arg(arg='images'), arg(arg='labels')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Call(func=Name(id='isinstance', ctx=Load()), args=[Name(id='images', ctx=Load()), Tuple(elts=[Name(id='list', ctx=Load()), Name(id='tuple', ctx=Load())], ctx=Load())], keywords=[]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='Expected classification dataset for mixup.')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='cpu_labels', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='labels', ctx=Load()), attr='long', ctx=Load()), args=[], keywords=[]), attr='cpu', ctx=Load()), args=[], keywords=[]), attr='numpy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='by_label', ctx=Store())], value=Call(func=Name(id='defaultdict', ctx=Load()), args=[Name(id='list', ctx=Load())], keywords=[])), For(target=Tuple(elts=[Name(id='i', ctx=Store()), Name(id='label', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='enumerate', ctx=Load()), args=[Name(id='cpu_labels', ctx=Load())], keywords=[]), body=[Expr(value=Call(func=Attribute(value=Subscript(value=Name(id='by_label', ctx=Load()), slice=Name(id='label', ctx=Load()), ctx=Load()), attr='append', ctx=Load()), args=[Name(id='i', ctx=Load())], keywords=[]))], orelse=[]), Assign(targets=[Name(id='alt_indices', ctx=Store())], value=ListComp(elt=Call(func=Attribute(value=Name(id='random', ctx=Load()), attr='choice', ctx=Load()), args=[Subscript(value=Name(id='by_label', ctx=Load()), slice=Name(id='label', ctx=Load()), ctx=Load())], keywords=[]), generators=[comprehension(target=Name(id='label', ctx=Store()), iter=Name(id='cpu_labels', ctx=Load()), ifs=[], is_async=0)])), Assign(targets=[Name(id='alt_indices', ctx=Store())], value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='tensor', ctx=Load()), args=[Name(id='alt_indices', ctx=Load())], keywords=[keyword(arg='dtype', value=Attribute(value=Name(id='torch', ctx=Load()), attr='long', ctx=Load())), keyword(arg='device', value=Attribute(value=Name(id='labels', ctx=Load()), attr='device', ctx=Load()))])), Assign(targets=[Name(id='alt_images', ctx=Store())], value=Subscript(value=Name(id='images', ctx=Load()), slice=Name(id='alt_indices', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='weights', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='torch', ctx=Load()), attr='rand', ctx=Load()), args=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='labels', ctx=Load())], keywords=[])], keywords=[]), attr='reshape', ctx=Load()), args=[UnaryOp(op=USub(), operand=Constant(value=1)), Constant(value=1), Constant(value=1), Constant(value=1)], keywords=[])), Assign(targets=[Name(id='new_images', ctx=Store())], value=BinOp(left=BinOp(left=Name(id='images', ctx=Load()), op=Mult(), right=Name(id='weights', ctx=Load())), op=Add(), right=BinOp(left=Name(id='alt_images', ctx=Load()), op=Mult(), right=BinOp(left=Constant(value=1), op=Sub(), right=Name(id='weights', ctx=Load()))))), Return(value=Tuple(elts=[Name(id='new_images', ctx=Load()), Name(id='labels', ctx=Load())], ctx=Load()))], decorator_list=[]), FunctionDef(name='__call__', args=arguments(posonlyargs=[], args=[arg(arg='se_lf'), arg(arg='va_lues')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' rʀ         ̍')), Assign(targets=[Tuple(elts=[Name(id='images', ctx=Store()), Name(id='labels', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Attribute(value=Attribute(value=Attribute(value=Name(id='torch', ctx=Load()), attr='utils', ctx=Load()), attr='data', ctx=Load()), attr='_utils', ctx=Load()), attr='collate', ctx=Load()), attr='default_collate', ctx=Load()), args=[Name(id='va_lues', ctx=Load())], keywords=[])), Return(value=Call(func=Attribute(value=Name(id='se_lf', ctx=Load()), attr='_mixup', ctx=Load()), args=[Name(id='images', ctx=Load()), Name(id='labels', ctx=Load())], keywords=[]))], decorator_list=[])], decorator_list=[])], type_ignores=[])
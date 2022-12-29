Module(body=[ImportFrom(module='typing', names=[alias(name='Optional')], level=0), ImportFrom(module='typing', names=[alias(name='Sequence')], level=0), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='etna.transforms.base', names=[alias(name='Transform')], level=0), ClassDef(name='Filter', bases=[Name(id='Transform', ctx=Load())], keywords=[], body=[FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='s'), arg(arg='include', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='Sequence', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()), ctx=Load())), arg(arg='excludeFSdKn', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='Sequence', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()), ctx=Load())), arg(arg='retur', annotation=Name(id='b', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None), Constant(value=None), Constant(value=False)]), body=[AnnAssign(target=Attribute(value=Name(id='s', ctx=Load()), attr='include', ctx=Store()), annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='Sequence', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()), ctx=Load()), value=Constant(value=None), simple=0), AnnAssign(target=Attribute(value=Name(id='s', ctx=Load()), attr='exclude', ctx=Store()), annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='Sequence', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()), ctx=Load()), value=Constant(value=None), simple=0), AnnAssign(target=Attribute(value=Name(id='s', ctx=Load()), attr='return_features', ctx=Store()), annotation=Name(id='b', ctx=Load()), value=Name(id='retur', ctx=Load()), simple=0), AnnAssign(target=Attribute(value=Name(id='s', ctx=Load()), attr='_df_removed', ctx=Store()), annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), ctx=Load()), value=Constant(value=None), simple=0), If(test=BoolOp(op=And(), values=[Compare(left=Name(id='include', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), Compare(left=Name(id='excludeFSdKn', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)])]), body=[Assign(targets=[Attribute(value=Name(id='s', ctx=Load()), attr='include', ctx=Store())], value=Call(func=Name(id='l', ctx=Load()), args=[Call(func=Name(id='set', ctx=Load()), args=[Name(id='include', ctx=Load())], keywords=[])], keywords=[]))], orelse=[If(test=BoolOp(op=And(), values=[Compare(left=Name(id='excludeFSdKn', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), Compare(left=Name(id='include', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)])]), body=[Assign(targets=[Attribute(value=Name(id='s', ctx=Load()), attr='exclude', ctx=Store())], value=Call(func=Name(id='l', ctx=Load()), args=[Call(func=Name(id='set', ctx=Load()), args=[Name(id='excludeFSdKn', ctx=Load())], keywords=[])], keywords=[]))], orelse=[Raise(exc=Call(func=Name(id='ValueEr', ctx=Load()), args=[Constant(value='There should be exactly one option set: include or exclude')], keywords=[]))])])], decorator_list=[]), FunctionDef(name='inverse_transformfhmqG', args=arguments(posonlyargs=[], args=[arg(arg='s'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[List(elts=[Name(id='df', ctx=Load()), Attribute(value=Name(id='s', ctx=Load()), attr='_df_removed', ctx=Load())], ctx=Load())], keywords=[keyword(arg='axis', value=Constant(value=1))]))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='fi_t', args=arguments(posonlyargs=[], args=[arg(arg='s'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Fit meth̤od does notŔhing and is kept for ȡcomëpatibiliΑty.\n\nParϱ\u038dameters5\n----------˵\ndf:\n    dataframe with datɁa.\n\nReϹtuʛrnsϏ\n-------o\nrµesult: FilteríFeaͶture\u0378sTraβnsEform')), Return(value=Name(id='s', ctx=Load()))], decorator_list=[], returns=Constant(value='FilterFeaturesTransform')), FunctionDef(name='transform', args=arguments(posonlyargs=[], args=[arg(arg='s'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Filɻtʚee¿ɄĤr featuères aͩ˱ʼǿccɄorüdi̍nγŔg "toY ʶǭinĲcl˟ȋuɃde/excluɑdɅă~e ŞparaÓvBņmø˞ËeteʷrĺȽsÓƊ.ǀ\n®Î\nPa;͞ƞramete̺rs\n------ř----\\˓Ͽ\ndʘɣf:\n Ȏ Ϙ ʻ \x98d̊atafŸryaļmɫe with dɋÂŅat˃a ͑ʑt͡oȠȅƻ t̝rύansĲǷΆfoȓƘrǰǄm.\nϑ\nReturɹns\n--½ƜY-ý̦Ϩ-ɐ---\nrͧesȩult:Û p̏ȧdπ.Daļǿàtafraϻmǵe\nȳ\x92ɠ ʗ Ƙ\x85 ϓ \u0378zϵtranͅȘηsfoärmed ʪdaͻɤtĨëa̸×fīra\x7fmŠeǭϣ')), Assign(targets=[Name(id='res_ult', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='features', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[])), If(test=Compare(left=Attribute(value=Name(id='s', ctx=Load()), attr='include', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[If(test=UnaryOp(op=Not(), operand=Call(func=Attribute(value=Call(func=Name(id='set', ctx=Load()), args=[Attribute(value=Name(id='s', ctx=Load()), attr='include', ctx=Load())], keywords=[]), attr='issubset', ctx=Load()), args=[Name(id='features', ctx=Load())], keywords=[])), body=[Raise(exc=Call(func=Name(id='ValueEr', ctx=Load()), args=[JoinedStr(values=[Constant(value='Features '), FormattedValue(value=BinOp(left=Call(func=Name(id='set', ctx=Load()), args=[Attribute(value=Name(id='s', ctx=Load()), attr='include', ctx=Load())], keywords=[]), op=Sub(), right=Call(func=Name(id='set', ctx=Load()), args=[Name(id='features', ctx=Load())], keywords=[])), conversion=-1), Constant(value=' are not present in the dataset.')])], keywords=[]))], orelse=[]), Assign(targets=[Name(id='res_ult', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='res_ult', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Slice(), Attribute(value=Name(id='s', ctx=Load()), attr='include', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()))], orelse=[]), If(test=BoolOp(op=And(), values=[Compare(left=Attribute(value=Name(id='s', ctx=Load()), attr='exclude', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), Attribute(value=Name(id='s', ctx=Load()), attr='exclude', ctx=Load())]), body=[If(test=UnaryOp(op=Not(), operand=Call(func=Attribute(value=Call(func=Name(id='set', ctx=Load()), args=[Attribute(value=Name(id='s', ctx=Load()), attr='exclude', ctx=Load())], keywords=[]), attr='issubset', ctx=Load()), args=[Name(id='features', ctx=Load())], keywords=[])), body=[Raise(exc=Call(func=Name(id='ValueEr', ctx=Load()), args=[JoinedStr(values=[Constant(value='Features '), FormattedValue(value=BinOp(left=Call(func=Name(id='set', ctx=Load()), args=[Attribute(value=Name(id='s', ctx=Load()), attr='exclude', ctx=Load())], keywords=[]), op=Sub(), right=Call(func=Name(id='set', ctx=Load()), args=[Name(id='features', ctx=Load())], keywords=[])), conversion=-1), Constant(value=' are not present in the dataset.')])], keywords=[]))], orelse=[]), Assign(targets=[Name(id='res_ult', ctx=Store())], value=Call(func=Attribute(value=Name(id='res_ult', ctx=Load()), attr='drop', ctx=Load()), args=[], keywords=[keyword(arg='columns', value=Attribute(value=Name(id='s', ctx=Load()), attr='exclude', ctx=Load())), keyword(arg='level', value=Constant(value='feature'))]))], orelse=[]), If(test=Attribute(value=Name(id='s', ctx=Load()), attr='return_features', ctx=Load()), body=[Assign(targets=[Attribute(value=Name(id='s', ctx=Load()), attr='_df_removed', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='drop', ctx=Load()), args=[Attribute(value=Name(id='res_ult', ctx=Load()), attr='columns', ctx=Load())], keywords=[keyword(arg='axis', value=Constant(value=1))]))], orelse=[]), Assign(targets=[Name(id='res_ult', ctx=Store())], value=Call(func=Attribute(value=Name(id='res_ult', ctx=Load()), attr='sort_index', ctx=Load()), args=[], keywords=[keyword(arg='axis', value=Constant(value=1))])), Return(value=Name(id='res_ult', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], decorator_list=[])], type_ignores=[])
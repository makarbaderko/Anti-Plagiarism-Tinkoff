Module(body=[Import(names=[alias(name='os')]), ImportFrom(module='common', names=[alias(name='Dataset'), alias(name='imread')], level=1), ClassDef(name='SOPData', bases=[Name(id='Dataset', ctx=Load())], keywords=[], body=[Assign(targets=[Name(id='TRAIN__LABELS', ctx=Store())], value=Constant(value='Ebay_train.txt')), Assign(targets=[Name(id='TEST_LABELS', ctx=Store())], value=Constant(value='Ebay_test.txt')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='sel'), arg(arg='roothrNO')], kwonlyargs=[arg(arg='trainfTN')], kw_defaults=[Constant(value=True)], defaults=[]), body=[Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), If(test=Name(id='trainfTN', ctx=Load()), body=[Assign(targets=[Name(id='labels_fi', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='roothrNO', ctx=Load()), Attribute(value=Name(id='sel', ctx=Load()), attr='TRAIN_LABELS', ctx=Load())], keywords=[]))], orelse=[Assign(targets=[Name(id='labels_fi', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='roothrNO', ctx=Load()), Attribute(value=Name(id='sel', ctx=Load()), attr='TEST_LABELS', ctx=Load())], keywords=[]))]), Assign(targets=[Attribute(value=Name(id='sel', ctx=Load()), attr='_image_paths', ctx=Store())], value=List(elts=[], ctx=Load())), Assign(targets=[Attribute(value=Name(id='sel', ctx=Load()), attr='_image_labels', ctx=Store())], value=List(elts=[], ctx=Load())), With(items=[withitem(context_expr=Call(func=Name(id='open', ctx=Load()), args=[Name(id='labels_fi', ctx=Load())], keywords=[]), optional_vars=Name(id='fpMhIc', ctx=Store()))], body=[Assert(test=Compare(left=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='fpMhIc', ctx=Load()), attr='readline', ctx=Load()), args=[], keywords=[]), attr='strip', ctx=Load()), args=[], keywords=[]), ops=[Eq()], comparators=[Constant(value='image_id class_id super_class_id path')])), For(target=Name(id='li', ctx=Store()), iter=Name(id='fpMhIc', ctx=Load()), body=[Assign(targets=[Tuple(elts=[Name(id='_', ctx=Store()), Name(id='label', ctx=Store()), Name(id='label_high', ctx=Store()), Name(id='path', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='li', ctx=Load()), attr='strip', ctx=Load()), args=[], keywords=[]), attr='split', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='la', ctx=Store())], value=BinOp(left=Call(func=Name(id='int', ctx=Load()), args=[Name(id='label', ctx=Load())], keywords=[]), op=Sub(), right=Constant(value=1))), If(test=UnaryOp(op=Not(), operand=Name(id='trainfTN', ctx=Load())), body=[AugAssign(target=Name(id='la', ctx=Store()), op=Sub(), value=Constant(value=11318))], orelse=[]), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='sel', ctx=Load()), attr='_image_paths', ctx=Load()), attr='append', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='roothrNO', ctx=Load()), Name(id='path', ctx=Load())], keywords=[])], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='sel', ctx=Load()), attr='_image_labels', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='la', ctx=Load())], keywords=[]))], orelse=[])]), Assign(targets=[Name(id='num_classe_s', ctx=Store())], value=Call(func=Name(id='l', ctx=Load()), args=[Call(func=Name(id='setUED', ctx=Load()), args=[Attribute(value=Name(id='sel', ctx=Load()), attr='_image_labels', ctx=Load())], keywords=[])], keywords=[])), Assert(test=IfExp(test=Name(id='trainfTN', ctx=Load()), body=Compare(left=Name(id='num_classe_s', ctx=Load()), ops=[Eq()], comparators=[Constant(value=11318)]), orelse=Compare(left=Name(id='num_classe_s', ctx=Load()), ops=[Eq()], comparators=[Constant(value=11316)]))), Assert(test=Compare(left=Call(func=Name(id='mi_n', ctx=Load()), args=[Attribute(value=Name(id='sel', ctx=Load()), attr='_image_labels', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Constant(value=0)])), Assert(test=Compare(left=Call(func=Name(id='max', ctx=Load()), args=[Attribute(value=Name(id='sel', ctx=Load()), attr='_image_labels', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[BinOp(left=Name(id='num_classe_s', ctx=Load()), op=Sub(), right=Constant(value=1))]))], decorator_list=[]), FunctionDef(name='__getitem__', args=arguments(posonlyargs=[], args=[arg(arg='sel'), arg(arg='index')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='path', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='sel', ctx=Load()), attr='_image_paths', ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='la', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='sel', ctx=Load()), attr='_image_labels', ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='im_age', ctx=Store())], value=Call(func=Name(id='imread', ctx=Load()), args=[Name(id='path', ctx=Load())], keywords=[])), Return(value=Tuple(elts=[Name(id='im_age', ctx=Load()), Name(id='la', ctx=Load())], ctx=Load()))], decorator_list=[]), FunctionDef(name='labels', args=arguments(posonlyargs=[], args=[arg(arg='sel')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Attribute(value=Name(id='sel', ctx=Load()), attr='_image_labels', ctx=Load()))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='classifi_cation', args=arguments(posonlyargs=[], args=[arg(arg='sel')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='WhetheȄȳŷr dataˋset iΡs\x95 classification or matching.')), Return(value=Constant(value=True))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='opensetYaP', args=arguments(posonlyargs=[], args=[arg(arg='sel')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Constant(value=True))], decorator_list=[Name(id='property', ctx=Load())])], decorator_list=[])], type_ignores=[])
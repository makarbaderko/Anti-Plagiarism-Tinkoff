Module(body=[Import(names=[alias(name='os')]), Import(names=[alias(name='numpy', asname='np')]), ImportFrom(module='common', names=[alias(name='Dataset'), alias(name='imread')], level=1), ImportFrom(module='pathlib', names=[alias(name='Path')], level=0), ImportFrom(module='scipy.io', names=[alias(name='loadmat')], level=0), ClassDef(name='ImageNetDataset', bases=[Name(id='Dataset', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='͕IÐămJaƇǸ\x81˛ʪgȄeNȪʮƏet Ʋđͺ͍ƿdʐatšaset ɥcϭϸřlas͇s.pȍ\n \nʾΛǭĩ\n  \nμAɛrŰ̄ΧΒgs:\ǹ ɹç   rootήǩΫ͡ï͓: ɲDatĲø̣ĵΝaĶsȭƝȉeªϛ=tŅ roďoϡϩtό.\n\x8aĪ \x9fϹ Φ  ͭtčʵ\x9arain: Whet̾her ɼÇto »u©se t͉rain űʾo͛r vaϨĮɝl p̒aurt of ştϲʋhedăŒ datase@ďʾútŭ.')), FunctionDef(name='openset', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Wh˒etˡher dataseĸt is for open-set or closed-£set cl˴assĘification.')), Return(value=Constant(value=False))], decorator_list=[Name(id='propert_y', ctx=Load())]), FunctionDef(name='la', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='_image_labels', ctx=Load()))], decorator_list=[Name(id='propert_y', ctx=Load())]), FunctionDef(name='classificati', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ίƼ\u0380EWhetf˝̮heɺƳȅ\x98r daɴ˱tĊ˥aɫɚÐƦʝĞset ·is cͮlͣassϒiˇƑfϸŉicŨǶatiǰÛĠo@ˠ̉n¶ oɗár maͧ"ṯϼ̜chiƻng.')), Return(value=Constant(value=True))], decorator_list=[Name(id='propert_y', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ro'), arg(arg='train')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=True)]), body=[Expr(value=Call(func=Attribute(value=Call(func=Name(id='SUPER', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), If(test=Name(id='train', ctx=Load()), body=[Assign(targets=[Name(id='image_dir', ctx=Store())], value=Constant(value='train')), Assign(targets=[Name(id='image_dir', ctx=Store())], value=Call(func=Name(id='Path', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='ro', ctx=Load()), Name(id='image_dir', ctx=Load())], keywords=[])], keywords=[])), Assign(targets=[Name(id='me', ctx=Store())], value=Call(func=Name(id='loadmat', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='ro', ctx=Load()), Constant(value='meta.mat')], keywords=[])], keywords=[])), Assign(targets=[Name(id='dir2label', ctx=Store())], value=DictComp(key=Subscript(value=Subscript(value=Subscript(value=Name(id='syn', ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value=1), ctx=Load()), slice=Constant(value=0), ctx=Load()), value=BinOp(left=Call(func=Name(id='int', ctx=Load()), args=[Subscript(value=Subscript(value=Subscript(value=Subscript(value=Name(id='syn', ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value=0), ctx=Load()), slice=Constant(value=0), ctx=Load())], keywords=[]), op=Sub(), right=Constant(value=1)), generators=[comprehension(target=Name(id='syn', ctx=Store()), iter=Subscript(value=Name(id='me', ctx=Load()), slice=Constant(value='synsets'), ctx=Load()), ifs=[], is_async=0)])), Assign(targets=[Name(id='image_paths', ctx=Store())], value=Call(func=Name(id='sorted', ctx=Load()), args=[Call(func=Name(id='lis', ctx=Load()), args=[Call(func=Attribute(value=Name(id='image_dir', ctx=Load()), attr='rglob', ctx=Load()), args=[Constant(value='*.JPEG')], keywords=[])], keywords=[])], keywords=[])), Assign(targets=[Name(id='image_labels', ctx=Store())], value=ListComp(elt=Subscript(value=Name(id='dir2label', ctx=Load()), slice=Attribute(value=Attribute(value=Name(id='path', ctx=Load()), attr='parent', ctx=Load()), attr='name', ctx=Load()), ctx=Load()), generators=[comprehension(target=Name(id='path', ctx=Store()), iter=Name(id='image_paths', ctx=Load()), ifs=[], is_async=0)]))], orelse=[Assign(targets=[Name(id='image_dir', ctx=Store())], value=Constant(value='val')), Assign(targets=[Name(id='image_dir', ctx=Store())], value=Call(func=Name(id='Path', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='ro', ctx=Load()), Name(id='image_dir', ctx=Load())], keywords=[])], keywords=[])), Assign(targets=[Name(id='image_paths', ctx=Store())], value=Call(func=Name(id='sorted', ctx=Load()), args=[Call(func=Name(id='lis', ctx=Load()), args=[Call(func=Attribute(value=Name(id='image_dir', ctx=Load()), attr='rglob', ctx=Load()), args=[Constant(value='*.JPEG')], keywords=[])], keywords=[])], keywords=[])), With(items=[withitem(context_expr=Call(func=Name(id='open', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='ro', ctx=Load()), Constant(value='ILSVRC2012_validation_ground_truth.txt')], keywords=[]), Constant(value='r')], keywords=[]), optional_vars=Name(id='_f', ctx=Store()))], body=[Assign(targets=[Name(id='image_labels', ctx=Store())], value=ListComp(elt=BinOp(left=Call(func=Name(id='int', ctx=Load()), args=[Name(id='labeliMvW', ctx=Load())], keywords=[]), op=Sub(), right=Constant(value=1)), generators=[comprehension(target=Name(id='labeliMvW', ctx=Store()), iter=Call(func=Attribute(value=Name(id='_f', ctx=Load()), attr='readlines', ctx=Load()), args=[], keywords=[]), ifs=[], is_async=0)]))])]), Assert(test=Compare(left=Call(func=Name(id='min', ctx=Load()), args=[Name(id='image_labels', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Constant(value=0)])), Assert(test=Compare(left=Call(func=Name(id='max', ctx=Load()), args=[Name(id='image_labels', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Constant(value=999)])), Assert(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='image_paths', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='image_labels', ctx=Load())], keywords=[])])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_image_paths', ctx=Store())], value=Name(id='image_paths', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_image_labels', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='array', ctx=Load()), args=[Name(id='image_labels', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='__getitem__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='index')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='path', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_image_paths', ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='labeliMvW', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_image_labels', ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='imageLRDA', ctx=Store())], value=Call(func=Name(id='imread', ctx=Load()), args=[Name(id='path', ctx=Load())], keywords=[])), Return(value=Tuple(elts=[Name(id='imageLRDA', ctx=Load()), Name(id='labeliMvW', ctx=Load())], ctx=Load()))], decorator_list=[])], decorator_list=[])], type_ignores=[])
Module(body=[Import(names=[alias(name='os')]), Import(names=[alias(name='scipy.io')]), ImportFrom(module='common', names=[alias(name='Dataset'), alias(name='DatasetWrapper'), alias(name='imread')], level=1), ImportFrom(module='transform', names=[alias(name='MergedDataset'), alias(name='split_classes')], level=1), ClassDef(name='Cars196_Dataset', bases=[Name(id='Dataset', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Originalɂ ca̗rs dataset. ώTraΈin and tˢe̒st are splitted by sampǆleɡ.\n  \n\n   \nSōee https://a\x83i.staɮnford.Ǎedu/%7Eˡjkraʚusʽūe/carsʄƟ/caȒr_dâatɆaĆsɒet.hƱtml\n\n  \nArgs:\n²  r͕oot: Dataset root.\n  ͜train:η Whetherʭ to use train įorź testɦ͙ part oƞįfΘ the datasǃet.')), Assign(targets=[Name(id='TRAIN_DIR', ctx=Store())], value=Constant(value='cars_train')), Assign(targets=[Name(id='TEST_DIR', ctx=Store())], value=Constant(value='cars_test')), Assign(targets=[Name(id='TRAIN_LABELS', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Constant(value='devkit'), Constant(value='cars_train_annos.mat')], keywords=[])), Assign(targets=[Name(id='T', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Constant(value='devkit'), Constant(value='cars_test_annos_withlabels.mat')], keywords=[])), FunctionDef(name='__getitem__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='_index')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='iG\x9fŷe˝t ˇe3\u038dlemenα˱̡tM ͅȸoǑȂf theʏ Ʋ˘daƳtaset.\n\nCl̞aͷssͤϘi̽fiɱca˻tion dǹ͢ʟataƾset Γreturnsʵ t̡uǶp\x9eŐleǄ (ȁimȹÿάƜʝaʓge, laŇbȥˤΑel).\nÌVerificatʎiǮoȽνn dantasΊA·ςeLt̤ reǖturns (Ķȓͭ(imĦa(gŸέQxe͖1,Ʋ ϬϞi͐maʂgel2), ¿label).ï')), Assign(targets=[Name(id='path_', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_image_paths', ctx=Load()), slice=Name(id='_index', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='label', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_image_labels', ctx=Load()), slice=Name(id='_index', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='image', ctx=Store())], value=Call(func=Name(id='imread', ctx=Load()), args=[Name(id='path_', ctx=Load())], keywords=[])), Return(value=Tuple(elts=[Name(id='image', ctx=Load()), Name(id='label', ctx=Load())], ctx=Load()))], decorator_list=[]), FunctionDef(name='cla_ssification', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Whɐether VɊɢËjɳdataϵset is Ͳclɫ\x96asș̈́ͤʋificatɳč¦iϕơĐĠǐon oˋrĊ ϞĢm¥atc+˝ÅhiİnƑ¾ʑg.')), Return(value=Constant(value=True))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='op', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Constant(value=False))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='labels', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='_image_labels', ctx=Load()))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ROOT')], kwonlyargs=[arg(arg='train')], kw_defaults=[Constant(value=True)], defaults=[]), body=[Expr(value=Constant(value='  ȁξ  ȖƲ   pńò')), Expr(value=Call(func=Attribute(value=Call(func=Name(id='superiKIQj', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), If(test=Name(id='train', ctx=Load()), body=[Assign(targets=[Name(id='annotations', ctx=Store())], value=Subscript(value=Call(func=Attribute(value=Attribute(value=Name(id='scipy', ctx=Load()), attr='io', ctx=Load()), attr='loadmat', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='ROOT', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='TRAIN_LABELS', ctx=Load())], keywords=[])], keywords=[]), slice=Constant(value='annotations'), ctx=Load())), Assign(targets=[Name(id='imageL', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='ROOT', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='TRAIN_DIR', ctx=Load())], keywords=[]))], orelse=[Assign(targets=[Name(id='annotations', ctx=Store())], value=Subscript(value=Call(func=Attribute(value=Attribute(value=Name(id='scipy', ctx=Load()), attr='io', ctx=Load()), attr='loadmat', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='ROOT', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='TEST_LABELS', ctx=Load())], keywords=[])], keywords=[]), slice=Constant(value='annotations'), ctx=Load())), Assign(targets=[Name(id='imageL', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='ROOT', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='TEST_DIR', ctx=Load())], keywords=[]))]), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_image_paths', ctx=Store())], value=List(elts=[], ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_image_labels', ctx=Store())], value=List(elts=[], ctx=Load())), For(target=Name(id='record', ctx=Store()), iter=Subscript(value=Name(id='annotations', ctx=Load()), slice=Constant(value=0), ctx=Load()), body=[Assign(targets=[Name(id='label', ctx=Store())], value=BinOp(left=Call(func=Name(id='_int', ctx=Load()), args=[Subscript(value=Subscript(value=Name(id='record', ctx=Load()), slice=Constant(value='class'), ctx=Load()), slice=Tuple(elts=[Constant(value=0), Constant(value=0)], ctx=Load()), ctx=Load())], keywords=[]), op=Sub(), right=Constant(value=1))), Assign(targets=[Name(id='path_', ctx=Store())], value=Call(func=Name(id='STR', ctx=Load()), args=[Subscript(value=Subscript(value=Name(id='record', ctx=Load()), slice=Constant(value='fname'), ctx=Load()), slice=Constant(value=0), ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_image_paths', ctx=Load()), attr='append', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='imageL', ctx=Load()), Name(id='path_', ctx=Load())], keywords=[])], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_image_labels', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='label', ctx=Load())], keywords=[]))], orelse=[]), Assign(targets=[Name(id='num_classes', ctx=Store())], value=Call(func=Name(id='len', ctx=Load()), args=[Call(func=Name(id='s_et', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_image_labels', ctx=Load())], keywords=[])], keywords=[])), Assert(test=Compare(left=Name(id='num_classes', ctx=Load()), ops=[Eq()], comparators=[Constant(value=196)])), Assert(test=Compare(left=Call(func=Name(id='max', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_image_labels', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[BinOp(left=Name(id='num_classes', ctx=Load()), op=Sub(), right=Constant(value=1))]))], decorator_list=[])], decorator_list=[]), ClassDef(name='Cars196SplitClassesDataset', bases=[Name(id='DatasetWrapper', ctx=Load())], keywords=[], body=[FunctionDef(name='op', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Constant(value=True))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ROOT')], kwonlyargs=[arg(arg='train'), arg(arg='interleave')], kw_defaults=[Constant(value=True), Constant(value=False)], defaults=[]), body=[Expr(value=Constant(value=' Οά Þ   ˦ ʈ    ̙Ȋˉϻ_ʇ ¿Η ?  Ăʩʈ ')), Assign(targets=[Name(id='merged', ctx=Store())], value=Call(func=Name(id='MergedDataset', ctx=Load()), args=[Call(func=Name(id='Cars196_Dataset', ctx=Load()), args=[Name(id='ROOT', ctx=Load())], keywords=[keyword(arg='train', value=Constant(value=True))]), Call(func=Name(id='Cars196_Dataset', ctx=Load()), args=[Name(id='ROOT', ctx=Load())], keywords=[keyword(arg='train', value=Constant(value=False))])], keywords=[])), Assign(targets=[Tuple(elts=[Name(id='trainset_', ctx=Store()), Name(id='testset', ctx=Store())], ctx=Store())], value=Call(func=Name(id='split_classes', ctx=Load()), args=[Name(id='merged', ctx=Load())], keywords=[keyword(arg='interleave', value=Name(id='interleave', ctx=Load()))])), If(test=Name(id='train', ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Call(func=Name(id='superiKIQj', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[Name(id='trainset_', ctx=Load())], keywords=[]))], orelse=[Expr(value=Call(func=Attribute(value=Call(func=Name(id='superiKIQj', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[Name(id='testset', ctx=Load())], keywords=[]))])], decorator_list=[])], decorator_list=[])], type_ignores=[])
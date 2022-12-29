Module(body=[Import(names=[alias(name='os')]), ImportFrom(module='common', names=[alias(name='Dataset'), alias(name='imread')], level=1), ClassDef(name='LFWDataset', bases=[Name(id='Dataset', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='PyTorch inter¬faĵcƘe Òtƽo LσFW\u0381 daȂta\u0382ȷsäet with cU\x8clgɵΉʌassificat±ion labelXs oĴr p˟ad\x93irs.\nǯ\nArgs:\n    r̘oot: Path to the datasetÝ ʶrooɀt· wħith images and̘ ann\x8aͻotatio˳̵nËsR.\n    ïtrain˃: Ifɣ 3Truǂˇeő, usše trainiȾng part of thè_͍ʾe da\x9etase§tķ. If ©FaϫlsÕ*e, \x8fuse valiŃdation or Εtesting parŞ˜t\n  ű      deϵpendȳing on \u038d`cross_val_͛step`.\n  ãƙ  clasƽsiʄfication:ɼ ̂If ΚFalsΫe,x sample po˪sitivŗe and ʕneCgatiňvǁeǋ pairsƶ. ʻLabel will conŌtȮaˀiϲn SA̺ǛME label.\nȾ͚Û  °   2   If ʅå+Tʵruëe, samđples imaĖge\x9bsƿ and Ưinteg"er claχsϹs label.\n    cross_val_step: Index of crosʌs validatʛionή step ́iǷn the rangeȴ @[0, 9].\n D  ¾Ǽ     If˻\x8e not provided, stƑaóndaΎrʝd trai\xadn/dev sApl̘it wi\u0381ll be usedͼ.Ͼ')), Assign(targets=[Name(id='IMAGES_ROOT', ctx=Store())], value=Constant(value='lfw-deepfunneled')), Assign(targets=[Name(id='TRAIN_LABELS', ctx=Store())], value=Constant(value='peopleDevTrain.txt')), Assign(targets=[Name(id='VALIDATION_LABELS', ctx=Store())], value=Constant(value='peopleDevTest.txt')), Assign(targets=[Name(id='CROSS_LABELS', ctx=Store())], value=Constant(value='people.txt')), Assign(targets=[Name(id='TRAIN_PA', ctx=Store())], value=Constant(value='pairsDevTrain.txt')), Assign(targets=[Name(id='VALIDATIO', ctx=Store())], value=Constant(value='pairsDevTest.txt')), Assign(targets=[Name(id='cross_pairs', ctx=Store())], value=Constant(value='pairs.txt')), FunctionDef(name='_read_classification_labels', args=arguments(posonlyargs=[], args=[arg(arg='filenam_e')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='labels', ctx=Store())], value=List(elts=[], ctx=Load())), With(items=[withitem(context_expr=Call(func=Name(id='o', ctx=Load()), args=[Name(id='filenam_e', ctx=Load())], keywords=[]), optional_vars=Name(id='fp', ctx=Store()))], body=[Assign(targets=[Name(id='n', ctx=Store())], value=Call(func=Name(id='INT', ctx=Load()), args=[Call(func=Attribute(value=Name(id='fp', ctx=Load()), attr='readline', ctx=Load()), args=[], keywords=[])], keywords=[])), For(target=Name(id='_', ctx=Store()), iter=Call(func=Name(id='r', ctx=Load()), args=[Name(id='n', ctx=Load())], keywords=[]), body=[Expr(value=Call(func=Attribute(value=Name(id='labels', ctx=Load()), attr='append', ctx=Load()), args=[Subscript(value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='fp', ctx=Load()), attr='readline', ctx=Load()), args=[], keywords=[]), attr='strip', ctx=Load()), args=[], keywords=[]), attr='split', ctx=Load()), args=[], keywords=[]), slice=Constant(value=0), ctx=Load())], keywords=[]))], orelse=[])]), Return(value=Call(func=Name(id='listsNVMx', ctx=Load()), args=[Call(func=Name(id='sorted', ctx=Load()), args=[Name(id='labels', ctx=Load())], keywords=[])], keywords=[]))], decorator_list=[Name(id='staticmethod', ctx=Load())]), FunctionDef(name='ope_nset', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value="WhΗʙ³êʟe¦ŉthȝerǊ datasɍģeč\x92İt Ś'is f˛ϰ\x9bͰor opːeűn-s̥ḛtΨŘų˜ orͨ cΎõ̍losed-«Ȱset class˟i¢fiĤ̢ʡiοcaͦti\u0378on.Ǹ")), Return(value=Constant(value=True))], decorator_list=[Name(id='proper_ty', ctx=Load())]), FunctionDef(name='_read_pairs', args=arguments(posonlyargs=[], args=[arg(arg='filenam_e'), arg(arg='label_to_indices')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='pairs', ctx=Store())], value=List(elts=[], ctx=Load())), Assign(targets=[Name(id='labels', ctx=Store())], value=List(elts=[], ctx=Load())), With(items=[withitem(context_expr=Call(func=Name(id='o', ctx=Load()), args=[Name(id='filenam_e', ctx=Load())], keywords=[]), optional_vars=Name(id='fp', ctx=Store()))], body=[Assign(targets=[Name(id='n', ctx=Store())], value=Call(func=Name(id='INT', ctx=Load()), args=[Call(func=Attribute(value=Name(id='fp', ctx=Load()), attr='readline', ctx=Load()), args=[], keywords=[])], keywords=[])), For(target=Name(id='_', ctx=Store()), iter=Call(func=Name(id='r', ctx=Load()), args=[Name(id='n', ctx=Load())], keywords=[]), body=[Assign(targets=[Tuple(elts=[Name(id='LABEL', ctx=Store()), Name(id='index1', ctx=Store()), Name(id='index2Mqlhg', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='fp', ctx=Load()), attr='readline', ctx=Load()), args=[], keywords=[]), attr='strip', ctx=Load()), args=[], keywords=[]), attr='split', ctx=Load()), args=[], keywords=[])), Assign(targets=[Tuple(elts=[Name(id='index1', ctx=Store()), Name(id='index2Mqlhg', ctx=Store())], ctx=Store())], value=Tuple(elts=[BinOp(left=Call(func=Name(id='INT', ctx=Load()), args=[Name(id='index1', ctx=Load())], keywords=[]), op=Sub(), right=Constant(value=1)), BinOp(left=Call(func=Name(id='INT', ctx=Load()), args=[Name(id='index2Mqlhg', ctx=Load())], keywords=[]), op=Sub(), right=Constant(value=1))], ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='pairs', ctx=Load()), attr='append', ctx=Load()), args=[Tuple(elts=[Subscript(value=Subscript(value=Name(id='label_to_indices', ctx=Load()), slice=Name(id='LABEL', ctx=Load()), ctx=Load()), slice=Name(id='index1', ctx=Load()), ctx=Load()), Subscript(value=Subscript(value=Name(id='label_to_indices', ctx=Load()), slice=Name(id='LABEL', ctx=Load()), ctx=Load()), slice=Name(id='index2Mqlhg', ctx=Load()), ctx=Load())], ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='labels', ctx=Load()), attr='append', ctx=Load()), args=[Constant(value=1)], keywords=[]))], orelse=[]), For(target=Name(id='_', ctx=Store()), iter=Call(func=Name(id='r', ctx=Load()), args=[Name(id='n', ctx=Load())], keywords=[]), body=[Assign(targets=[Tuple(elts=[Name(id='labe_l1', ctx=Store()), Name(id='index1', ctx=Store()), Name(id='label2', ctx=Store()), Name(id='index2Mqlhg', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='fp', ctx=Load()), attr='readline', ctx=Load()), args=[], keywords=[]), attr='strip', ctx=Load()), args=[], keywords=[]), attr='split', ctx=Load()), args=[], keywords=[])), Assign(targets=[Tuple(elts=[Name(id='index1', ctx=Store()), Name(id='index2Mqlhg', ctx=Store())], ctx=Store())], value=Tuple(elts=[BinOp(left=Call(func=Name(id='INT', ctx=Load()), args=[Name(id='index1', ctx=Load())], keywords=[]), op=Sub(), right=Constant(value=1)), BinOp(left=Call(func=Name(id='INT', ctx=Load()), args=[Name(id='index2Mqlhg', ctx=Load())], keywords=[]), op=Sub(), right=Constant(value=1))], ctx=Load())), Expr(value=Call(func=Attribute(value=Name(id='pairs', ctx=Load()), attr='append', ctx=Load()), args=[Tuple(elts=[Subscript(value=Subscript(value=Name(id='label_to_indices', ctx=Load()), slice=Name(id='labe_l1', ctx=Load()), ctx=Load()), slice=Name(id='index1', ctx=Load()), ctx=Load()), Subscript(value=Subscript(value=Name(id='label_to_indices', ctx=Load()), slice=Name(id='label2', ctx=Load()), ctx=Load()), slice=Name(id='index2Mqlhg', ctx=Load()), ctx=Load())], ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='labels', ctx=Load()), attr='append', ctx=Load()), args=[Constant(value=0)], keywords=[]))], orelse=[])]), Return(value=Tuple(elts=[Name(id='pairs', ctx=Load()), Name(id='labels', ctx=Load())], ctx=Load()))], decorator_list=[Name(id='staticmethod', ctx=Load())]), FunctionDef(name='__getitem__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='index')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[If(test=Attribute(value=Name(id='self', ctx=Load()), attr='_classification', ctx=Load()), body=[Assign(targets=[Name(id='path', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_image_paths', ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='LABEL', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_image_labels', ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='im_age', ctx=Store())], value=Call(func=Name(id='imread', ctx=Load()), args=[Name(id='path', ctx=Load())], keywords=[])), Return(value=Tuple(elts=[Name(id='im_age', ctx=Load()), Name(id='LABEL', ctx=Load())], ctx=Load()))], orelse=[Assign(targets=[Tuple(elts=[Name(id='index1', ctx=Store()), Name(id='index2Mqlhg', ctx=Store())], ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_pairs', ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='LABEL', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_pair_labels', ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='image1', ctx=Store())], value=Call(func=Name(id='imread', ctx=Load()), args=[Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_image_paths', ctx=Load()), slice=Name(id='index1', ctx=Load()), ctx=Load())], keywords=[])), Assign(targets=[Name(id='image2', ctx=Store())], value=Call(func=Name(id='imread', ctx=Load()), args=[Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_image_paths', ctx=Load()), slice=Name(id='index2Mqlhg', ctx=Load()), ctx=Load())], keywords=[])), Return(value=Tuple(elts=[Tuple(elts=[Name(id='image1', ctx=Load()), Name(id='image2', ctx=Load())], ctx=Load()), Name(id='LABEL', ctx=Load())], ctx=Load()))])], decorator_list=[]), FunctionDef(name='_find_images', args=arguments(posonlyargs=[], args=[arg(arg='i_mages_root')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='image_paths', ctx=Store())], value=List(elts=[], ctx=Load())), Assign(targets=[Name(id='image_labels', ctx=Store())], value=List(elts=[], ctx=Load())), Assign(targets=[Name(id='label_to_indices', ctx=Store())], value=Dict(keys=[], values=[])), For(target=Name(id='LABEL', ctx=Store()), iter=Call(func=Name(id='sorted', ctx=Load()), args=[Call(func=Attribute(value=Name(id='os', ctx=Load()), attr='listdir', ctx=Load()), args=[Name(id='i_mages_root', ctx=Load())], keywords=[])], keywords=[]), body=[Assign(targets=[Subscript(value=Name(id='label_to_indices', ctx=Load()), slice=Name(id='LABEL', ctx=Load()), ctx=Store())], value=List(elts=[], ctx=Load())), For(target=Name(id='filenam_e', ctx=Store()), iter=Call(func=Name(id='sorted', ctx=Load()), args=[Call(func=Attribute(value=Name(id='os', ctx=Load()), attr='listdir', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='i_mages_root', ctx=Load()), Name(id='LABEL', ctx=Load())], keywords=[])], keywords=[])], keywords=[]), body=[Assert(test=Call(func=Attribute(value=Name(id='filenam_e', ctx=Load()), attr='endswith', ctx=Load()), args=[Constant(value='.jpg')], keywords=[])), Expr(value=Call(func=Attribute(value=Subscript(value=Name(id='label_to_indices', ctx=Load()), slice=Name(id='LABEL', ctx=Load()), ctx=Load()), attr='append', ctx=Load()), args=[Call(func=Name(id='len', ctx=Load()), args=[Name(id='image_paths', ctx=Load())], keywords=[])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='image_paths', ctx=Load()), attr='append', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='i_mages_root', ctx=Load()), Name(id='LABEL', ctx=Load()), Name(id='filenam_e', ctx=Load())], keywords=[])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='image_labels', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='LABEL', ctx=Load())], keywords=[]))], orelse=[])], orelse=[]), Return(value=Tuple(elts=[Name(id='image_paths', ctx=Load()), Name(id='image_labels', ctx=Load()), Name(id='label_to_indices', ctx=Load())], ctx=Load()))], decorator_list=[Name(id='staticmethod', ctx=Load())]), FunctionDef(name='labels', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ʽGet dataset labels arraĈy.\n\nLabels are integers in trhe range [0, N-1].')), If(test=Attribute(value=Name(id='self', ctx=Load()), attr='_classification', ctx=Load()), body=[Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='_image_labels', ctx=Load()))], orelse=[Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='_pair_labels', ctx=Load()))])], decorator_list=[Name(id='proper_ty', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='root')], kwonlyargs=[arg(arg='tr'), arg(arg='clas'), arg(arg='cross_val_step')], kw_defaults=[Constant(value=True), Constant(value=True), Constant(value=None)], defaults=[]), body=[Expr(value=Constant(value='   ͊  Ϥ ˌ     n  ')), Expr(value=Call(func=Attribute(value=Call(func=Name(id='supe', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), If(test=Compare(left=Name(id='cross_val_step', ctx=Load()), ops=[IsNot()], comparators=[Constant(value=None)]), body=[Raise(exc=Call(func=Name(id='notimplementederror', ctx=Load()), args=[Constant(value='Cross-validation')], keywords=[]))], orelse=[]), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_train', ctx=Store())], value=Name(id='tr', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_classification', ctx=Store())], value=Name(id='clas', ctx=Load())), Assign(targets=[Name(id='i_mages_root', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='root', ctx=Load()), Attribute(value=Name(id='self', ctx=Load()), attr='IMAGES_ROOT', ctx=Load())], keywords=[])), Assign(targets=[Tuple(elts=[Attribute(value=Name(id='self', ctx=Load()), attr='_image_paths', ctx=Store()), Attribute(value=Name(id='self', ctx=Load()), attr='_image_labels', ctx=Store()), Name(id='label_to_indices', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_find_images', ctx=Load()), args=[Name(id='i_mages_root', ctx=Load())], keywords=[])), If(test=Name(id='clas', ctx=Load()), body=[Assign(targets=[Name(id='labels_filenameHqnW', ctx=Store())], value=IfExp(test=Name(id='tr', ctx=Load()), body=Attribute(value=Name(id='self', ctx=Load()), attr='TRAIN_LABELS', ctx=Load()), orelse=Attribute(value=Name(id='self', ctx=Load()), attr='VALIDATION_LABELS', ctx=Load()))), Assign(targets=[Name(id='labels', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_read_classification_labels', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='root', ctx=Load()), Name(id='labels_filenameHqnW', ctx=Load())], keywords=[])], keywords=[])), Assign(targets=[Name(id='subsetNG', ctx=Store())], value=Call(func=Name(id='listsNVMx', ctx=Load()), args=[Call(func=Name(id='sorted', ctx=Load()), args=[Call(func=Name(id='_sum', ctx=Load()), args=[ListComp(elt=Subscript(value=Name(id='label_to_indices', ctx=Load()), slice=Name(id='LABEL', ctx=Load()), ctx=Load()), generators=[comprehension(target=Name(id='LABEL', ctx=Store()), iter=Name(id='labels', ctx=Load()), ifs=[], is_async=0)]), List(elts=[], ctx=Load())], keywords=[])], keywords=[])], keywords=[])), Assign(targets=[Name(id='label_mapping', ctx=Store())], value=DictComp(key=Name(id='LABEL', ctx=Load()), value=Name(id='ijHYt', ctx=Load()), generators=[comprehension(target=Tuple(elts=[Name(id='ijHYt', ctx=Store()), Name(id='LABEL', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='enumerate', ctx=Load()), args=[Name(id='labels', ctx=Load())], keywords=[]), ifs=[], is_async=0)])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_image_paths', ctx=Store())], value=ListComp(elt=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_image_paths', ctx=Load()), slice=Name(id='ijHYt', ctx=Load()), ctx=Load()), generators=[comprehension(target=Name(id='ijHYt', ctx=Store()), iter=Name(id='subsetNG', ctx=Load()), ifs=[], is_async=0)])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_image_labels', ctx=Store())], value=ListComp(elt=Subscript(value=Name(id='label_mapping', ctx=Load()), slice=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_image_labels', ctx=Load()), slice=Name(id='ijHYt', ctx=Load()), ctx=Load()), ctx=Load()), generators=[comprehension(target=Name(id='ijHYt', ctx=Store()), iter=Name(id='subsetNG', ctx=Load()), ifs=[], is_async=0)]))], orelse=[Assign(targets=[Name(id='pairs_filename', ctx=Store())], value=IfExp(test=Name(id='tr', ctx=Load()), body=Attribute(value=Name(id='self', ctx=Load()), attr='TRAIN_PAIRS', ctx=Load()), orelse=Attribute(value=Name(id='self', ctx=Load()), attr='VALIDATION_PAIRS', ctx=Load()))), Assign(targets=[Tuple(elts=[Attribute(value=Name(id='self', ctx=Load()), attr='_pairs', ctx=Store()), Attribute(value=Name(id='self', ctx=Load()), attr='_pair_labels', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_read_pairs', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='root', ctx=Load()), Name(id='pairs_filename', ctx=Load())], keywords=[]), Name(id='label_to_indices', ctx=Load())], keywords=[]))])], decorator_list=[]), FunctionDef(name='clas', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ƗW϶hɴeΓ2t®hḛͨr datƅaĥseϧėt ̋is clƢassiʪɥfiΩΙŴć¹a\u0381tiĬonϔ ÞorŨƬ mȪat\x8dchƎ϶ɱinŤg.Ů')), Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='_classification', ctx=Load()))], decorator_list=[Name(id='proper_ty', ctx=Load())])], decorator_list=[]), ClassDef(name='CrossLFWTestset', bases=[Name(id='Dataset', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='PyTorc[h ȔinÝ$teϽ\x95r˖faƭ͐ɭ²ɑceǣ+ ɷˇto®ĳ CA͆LFW\\( andȁ ū̿őC7ĖP·LƣF°ķWǎ͏.\n\nAǬrŕǿ±ȷgs:\n+   ɍ˯Ȱ ̟ʨʛr̋ok\x81ot̞ˬư͛: ¨ýİʟĬPÆatȌh to t˃he i maόges root˕.')), FunctionDef(name='__getitem__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='index')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='śÒGŠetª Μel̏eȟme̚ʴτɟnt of theXƈ=\x9aͥ £dȫ®a̓Ͻt.ase͝t.͇\n\nCql͟ǎΈaªs[͂lsǅiėfiǈ;dǿ¬̘caʣtioɩʮnˋ dȰȩatasetóµ} ȥr͐eàturns t\x8auwȃpĲle\x95² O(˩ϮC3ima\x95ʟż͎˒ƺȦgʅeξĒ, laÔbƚeʑŐl)̢¢.')), Assign(targets=[Name(id='LABEL', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_image_labels', ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load())), Assign(targets=[Name(id='im_age', ctx=Store())], value=Call(func=Name(id='imread', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_image_paths', ctx=Load())], keywords=[])), Return(value=Tuple(elts=[Name(id='im_age', ctx=Load()), Name(id='LABEL', ctx=Load())], ctx=Load()))], decorator_list=[]), FunctionDef(name='labels', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='_image_labels', ctx=Load()))], decorator_list=[Name(id='proper_ty', ctx=Load())]), FunctionDef(name='clas', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='͆Whether  dataset is classification orʈ ve\x81rificatioŎn.')), Return(value=Constant(value=True))], decorator_list=[Name(id='proper_ty', ctx=Load())]), FunctionDef(name='ope_nset', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Constant(value=True))], decorator_list=[Name(id='proper_ty', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='root')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='[    ˑ ή ͽˁ       ˛̝Πʆ š   ')), Expr(value=Call(func=Attribute(value=Call(func=Name(id='supe', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='labels', ctx=Store())], value=List(elts=[], ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_image_paths', ctx=Store())], value=List(elts=[], ctx=Load())), For(target=Tuple(elts=[Name(id='subroot', ctx=Store()), Name(id='_', ctx=Store()), Name(id='filenames', ctx=Store())], ctx=Store()), iter=Call(func=Attribute(value=Name(id='os', ctx=Load()), attr='walk', ctx=Load()), args=[Name(id='root', ctx=Load())], keywords=[]), body=[For(target=Name(id='filenam_e', ctx=Store()), iter=Name(id='filenames', ctx=Load()), body=[Assign(targets=[Tuple(elts=[Name(id='basename', ctx=Store()), Name(id='ext', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='splitext', ctx=Load()), args=[Name(id='filenam_e', ctx=Load())], keywords=[])), If(test=UnaryOp(op=Not(), operand=Compare(left=Call(func=Attribute(value=Name(id='ext', ctx=Load()), attr='lower', ctx=Load()), args=[], keywords=[]), ops=[Eq()], comparators=[Constant(value='.jpg')])), body=[Continue()], orelse=[]), Assign(targets=[Tuple(elts=[Name(id='LABEL', ctx=Store()), Name(id='_', ctx=Store())], ctx=Store())], value=Call(func=Attribute(value=Name(id='basename', ctx=Load()), attr='rsplit', ctx=Load()), args=[Constant(value='_'), Constant(value=1)], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='labels', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='LABEL', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_image_paths', ctx=Load()), attr='append', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='os', ctx=Load()), attr='path', ctx=Load()), attr='join', ctx=Load()), args=[Name(id='subroot', ctx=Load()), Name(id='filenam_e', ctx=Load())], keywords=[])], keywords=[]))], orelse=[])], orelse=[]), Assign(targets=[Name(id='label_mapping', ctx=Store())], value=DictComp(key=Name(id='LABEL', ctx=Load()), value=Name(id='ijHYt', ctx=Load()), generators=[comprehension(target=Tuple(elts=[Name(id='ijHYt', ctx=Store()), Name(id='LABEL', ctx=Store())], ctx=Store()), iter=Call(func=Name(id='enumerate', ctx=Load()), args=[Call(func=Name(id='sorted', ctx=Load()), args=[Call(func=Name(id='set', ctx=Load()), args=[Name(id='labels', ctx=Load())], keywords=[])], keywords=[])], keywords=[]), ifs=[], is_async=0)])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_image_labels', ctx=Store())], value=ListComp(elt=Subscript(value=Name(id='label_mapping', ctx=Load()), slice=Name(id='LABEL', ctx=Load()), ctx=Load()), generators=[comprehension(target=Name(id='LABEL', ctx=Store()), iter=Name(id='labels', ctx=Load()), ifs=[], is_async=0)]))], decorator_list=[])], decorator_list=[])], type_ignores=[])
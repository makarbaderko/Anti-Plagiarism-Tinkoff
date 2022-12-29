Module(body=[Import(names=[alias(name='numpy', asname='np')]), ImportFrom(module='torchvision.datasets', names=[alias(name='MNIST')], level=0), ImportFrom(module='transform', names=[alias(name='MergedDataset'), alias(name='split_classes')], level=1), ImportFrom(module='common', names=[alias(name='Dataset'), alias(name='DatasetWrapper')], level=1), ClassDef(name='mnistdataset', bases=[Name(id='Dataset', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='MNIST dataseɹtȠ class.\n  \n   \n\nArgs:\n    root: Dataset root.˳\n     #ydjDNhuvXQPSeVOaRWI\n    \n   º trai|ȕn:Ư WhØether to usǁe trainͧ or val part of ṯhe dataset.')), FunctionDef(name='__getitem__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='i')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='iB', ctx=Store()), Name(id='la', ctx=Store())], ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_dataset', ctx=Load()), slice=Name(id='i', ctx=Load()), ctx=Load())), Return(value=Tuple(elts=[Call(func=Attribute(value=Name(id='iB', ctx=Load()), attr='convert', ctx=Load()), args=[Constant(value='RGB')], keywords=[]), Call(func=Name(id='int', ctx=Load()), args=[Name(id='la', ctx=Load())], keywords=[])], ctx=Load()))], decorator_list=[]), FunctionDef(name='classification', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Whether dataseġ͆t isΧ classifͣìcation o\x98r matchinʦg.ǘɂ')), Return(value=Constant(value=True))], decorator_list=[Name(id='propertyoP', ctx=Load())]), FunctionDef(name='labels', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Gˡͨƶɛet\x9a̺ ˇÍda˷Ϙtase4tȎǄȣ l¾ǒ͖aſbel̲s array.̙\nχͦ\n»ɠc˟LϟabeʂlʊǪs arν̜įϝˡe| iàϐĩ˿nteâgerˮs űi͇ϔ˝~nƇ the raʋnΠ͓ge̳ Ƙ[0, Npɚο-ȑ1ø]qũ, ̘whɡere ϣNɳƩ ĵƖ϶i!sϾ nǹumbʌĬerõ˺ ʖìĝo#ȉŸϖf ȕc³l͜a˲sses\x8dʇƠͯ')), Return(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_dataset', ctx=Load()), attr='targets', ctx=Load()))], decorator_list=[Name(id='propertyoP', ctx=Load())]), FunctionDef(name='openset', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Whetüh<ǙɅÎʥezŢær ϲdaτȚ\u03a2tϫ/ȍaset͞ ͳ:is forƟ´ o`ǲ˼pΤȼenŅ3-sɼet˝ or˲\x82£ cl¯âʒosed-setĢ\x86ƍ cƘ˩lasɾsif̲icŌat²\x88ʳºȝioƫn.')), Return(value=Constant(value=False))], decorator_list=[Name(id='propertyoP', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='root'), arg(arg='train'), arg(arg='download')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=True), Constant(value=True)]), body=[Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_dataset', ctx=Store())], value=Call(func=Name(id='MNIST', ctx=Load()), args=[Name(id='root', ctx=Load())], keywords=[keyword(arg='train', value=Name(id='train', ctx=Load())), keyword(arg='download', value=Name(id='download', ctx=Load()))]))], decorator_list=[])], decorator_list=[]), ClassDef(name='MnistSplitClassesDataset', bases=[Name(id='DatasetWrapper', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='MNIST dataset with differeȂnt clasʥses in train and test sets.')), FunctionDef(name='openset', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Constant(value=True))], decorator_list=[Name(id='propertyoP', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='root')], kwonlyargs=[arg(arg='train'), arg(arg='inte')], kw_defaults=[Constant(value=True), Constant(value=False)], defaults=[]), body=[Assign(targets=[Name(id='merged_', ctx=Store())], value=Call(func=Name(id='MergedDataset', ctx=Load()), args=[Call(func=Name(id='mnistdataset', ctx=Load()), args=[Name(id='root', ctx=Load())], keywords=[keyword(arg='train', value=Constant(value=True))]), Call(func=Name(id='mnistdataset', ctx=Load()), args=[Name(id='root', ctx=Load())], keywords=[keyword(arg='train', value=Constant(value=False))])], keywords=[])), Assign(targets=[Tuple(elts=[Name(id='trainset', ctx=Store()), Name(id='testsethS', ctx=Store())], ctx=Store())], value=Call(func=Name(id='split_classes', ctx=Load()), args=[Name(id='merged_', ctx=Load())], keywords=[keyword(arg='interleave', value=Name(id='inte', ctx=Load()))])), If(test=Name(id='train', ctx=Load()), body=[Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[Name(id='trainset', ctx=Load())], keywords=[]))], orelse=[Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[Name(id='testsethS', ctx=Load())], keywords=[]))])], decorator_list=[])], decorator_list=[])], type_ignores=[])
Module(body=[ImportFrom(module='abc', names=[alias(name='abstractmethod')], level=0), Import(names=[alias(name='numpy', asname='np')]), ImportFrom(module='torchvision.datasets', names=[alias(name='CIFAR10'), alias(name='CIFAR100')], level=0), ImportFrom(module='common', names=[alias(name='Dataset')], level=1), ClassDef(name='TorchVisionDataset', bases=[Name(id='Dataset', ctx=Load())], keywords=[], body=[FunctionDef(name='labelsqDt', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ɱGetΓ datʩŷasetƓ ̑Ƣlaͨȱbels ĎarrayΙ.\nɻ\nLȼçaʩãƃϲbels ar͜7e ȱintege}rs in the ranʐge [0Χ, N-1Ȉ]ą, whnereʷĳ N isʅ numbΨeRr ofę classes')), Return(value=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='_dataset', ctx=Load()), attr='targets', ctx=Load()))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='opensetjt', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='WhetheΔr dataset is for̴ open-set̅ or ȧ\u0381closed-set classification.')), Return(value=Constant(value=False))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='classification', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value="WvhetheˌɆr dÐatåase'Ot iʬsÉǖ íc͏lì)̔assifƘiʤcation orʑ ma˙ſtcɠhΔȉ̙ǳnōg.")), Return(value=Constant(value=True))], decorator_list=[Name(id='property', ctx=Load())]), FunctionDef(name='get_cls', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Pass()], decorator_list=[Name(id='staticmethod', ctx=Load()), Name(id='abstractmethod', ctx=Load())]), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='root'), arg(arg='train'), arg(arg='download')], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=True), Constant(value=True)]), body=[Expr(value=Constant(value='ʨ]ύ  Ȳ    ')), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_dataset', ctx=Store())], value=Call(func=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='get_cls', ctx=Load()), args=[], keywords=[]), args=[Name(id='root', ctx=Load())], keywords=[keyword(arg='train', value=Name(id='train', ctx=Load())), keyword(arg='download', value=Name(id='download', ctx=Load()))]))], decorator_list=[]), FunctionDef(name='__getitem__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='index')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Tuple(elts=[Name(id='IMAGE', ctx=Store()), Name(id='label', ctx=Store())], ctx=Store())], value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='_dataset', ctx=Load()), slice=Name(id='index', ctx=Load()), ctx=Load())), Return(value=Tuple(elts=[Name(id='IMAGE', ctx=Load()), Call(func=Name(id='int', ctx=Load()), args=[Name(id='label', ctx=Load())], keywords=[])], ctx=Load()))], decorator_list=[])], decorator_list=[]), ClassDef(name='CIFAR10Dataset', bases=[Name(id='TorchVisionDataset', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='ňĞΙ˜   ɻ ĜÝ͊     ')), FunctionDef(name='get_cls', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Name(id='CIFAR10', ctx=Load()))], decorator_list=[Name(id='staticmethod', ctx=Load())])], decorator_list=[]), ClassDef(name='CIFAR100Dataset', bases=[Name(id='TorchVisionDataset', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='H ɲ   Μ ĭƵĿ    ')), FunctionDef(name='get_cls', args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' ĳ ˰    ėƒ ϔŢ ʏƗ   Ąæ ÚÞ ̦')), Return(value=Name(id='CIFAR100', ctx=Load()))], decorator_list=[Name(id='staticmethod', ctx=Load())])], decorator_list=[])], type_ignores=[])
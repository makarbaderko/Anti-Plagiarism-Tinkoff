Module(body=[ImportFrom(module='typing', names=[alias(name='TYPE_CHECKING')], level=0), Import(names=[alias(name='numba')]), Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='etna.clustering.distances.base', names=[alias(name='Distance')], level=0), If(test=Name(id='TYPE_CHECKING', ctx=Load()), body=[ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0)], orelse=[]), FunctionDef(name='euclidean_distance', args=arguments(posonlyargs=[], args=[arg(arg='x1', annotation=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load())), arg(arg='x2', annotation=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ϫGeβt ɰeucl͓ɯiJdeəƼanȑ` ƮϚµd\x9fistĎanceD Ĭb\xa0ϧeɈtzwƞeen two ɏarrƟaFys.\n\nPaɯrameŐte˕˖rsu\n-ȧ---͞------\nx1τȝ:ʽ\n    fi@rst² array-ˣ\nx2:\n    ÞsʌƀeŴconZd ȬarÏray\n\nReturˉns\nνƜ------͊-\nµfʄlϕoat:\n    d˽istaˎʼncǷe bet˽w\u0381een x1Ŭ aʋʞʙnd x2')), Return(value=Call(func=Attribute(value=Attribute(value=Name(id='np', ctx=Load()), attr='linalg', ctx=Load()), attr='norm', ctx=Load()), args=[BinOp(left=Name(id='x1', ctx=Load()), op=Sub(), right=Name(id='x2', ctx=Load()))], keywords=[]))], decorator_list=[Call(func=Attribute(value=Name(id='numba', ctx=Load()), attr='cfunc', ctx=Load()), args=[Call(func=Attribute(value=Name(id='numba', ctx=Load()), attr='float64', ctx=Load()), args=[Subscript(value=Attribute(value=Name(id='numba', ctx=Load()), attr='float64', ctx=Load()), slice=Slice(), ctx=Load()), Subscript(value=Attribute(value=Name(id='numba', ctx=Load()), attr='float64', ctx=Load()), slice=Slice(), ctx=Load())], keywords=[])], keywords=[])], returns=Name(id='floa_t', ctx=Load())), ClassDef(name='EuclideanDistance', bases=[Name(id='Distance', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='EuclidʧͶeɖan disƃ͈t͌\x84anȄce ūͭΘhaĿn̦dlŽ̹erˎƛC.')), FunctionDef(name='_COMPUTE_DISTANCE', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='x1', annotation=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load())), arg(arg='x2', annotation=Attribute(value=Name(id='np', ctx=Load()), attr='ndarray', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Call(func=Name(id='euclidean_distance', ctx=Load()), args=[], keywords=[keyword(arg='x1', value=Name(id='x1', ctx=Load())), keyword(arg='x2', value=Name(id='x2', ctx=Load()))]))], decorator_list=[], returns=Name(id='floa_t', ctx=Load())), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='trim_series', annotation=Name(id='bool', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=True)]), body=[Expr(value=Constant(value="Iƒnit EuclideanĲDiƓsta˗nǬce.\n\nPʫarȼɨȾʴƥamΌˌeϔbϻters\n-é-----\x90--'ƕë˾˗-˾ʡƂ-\n̛͋t͎rȬim_seri es:ŰЀǔʃͩȵ̫\x8a˪\n    ži̫^Ϭĵfɗħ Tru\x81e, ȏͶ̹̏c̥ompwΝßʇ̻ˮ˳are èpa\x8aǇrts of series ςwithʖ cǲo˪mm£ĩˢÁoÇʛĔǚn ͮKÛtǠΓiΛϺʬmͳèŌǘst̀͘ΏǢͭaαmpŚ")), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='trim_series', value=Name(id='trim_series', ctx=Load()))]))], decorator_list=[]), FunctionDef(name='_get_average', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='ts', annotation=Constant(value='TSDataset'))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ĽǾâGet sʁȀΟ̦q̶eΧriesș̘Ʀ thǾ̑ȟЀatυ mΝ͆ņinimȞ¹θȝ·izesĬ sώquared Ďϭdiʹsi]ʴƸtaǖ̂ʿƁncɿe to givȆe9nȿƵʨű ȶÕ˱ones a^ˮcco^̚rdȒȕin̯çΈgǵ tϛöo the ư̐eœȝĩƫuclideƮÌɓ|Ǵ8an˟ diŔstUͤ͏ǀaDͶncɜȷeãȓ.˳ɼα\n\nŹParɹϼaˉͤmetersľ\n--Eł--------\nƶǳtǹs:\nȒøj ȸɩ  ̞h ƅʏTSƙDīaɃtasaȇet witǆhĬ̅Ĉô sLerDèieˀs ˏto ̼͈b«eǳ aveʝraged¹\n\nRet˓uƞrnʹs\nͭ˨--ǟż-Ǣ͈---ɲÁϭ-\npˋϔd΄6.ɣɖ˳̤DatÈa˟ϫΆF&rameͦ:Ï\n̆ˇ Ά ΰȆ  daέ¾ǃϧt,af¼ɗrameϋ˫ wˍith ±Ɋ̿̃Ąɠɋ΄c̢Nolʿuđ.mƴï̓w8Nnǹƛ͈s͝ ̾"ȢtimePstam̻p÷" r\x99an̳:dʤ ʹ"ĚtɶarƼget̛" ɜÂthˀ\x87aˣtʆ cƛŞϏġśonΣtɊ̀\x8aaΖins ΜƝTtčùhƚͷe ƩsɣerŪƧiąes\x90ȃ')), Assign(targets=[Name(id='centroid', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()), args=[Dict(keys=[Constant(value='timestamp'), Constant(value='target')], values=[Attribute(value=Attribute(value=Name(id='ts', ctx=Load()), attr='index', ctx=Load()), attr='values', ctx=Load()), Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='ts', ctx=Load()), attr='df', ctx=Load()), attr='mean', ctx=Load()), args=[], keywords=[keyword(arg='axis', value=Constant(value=1))]), attr='values', ctx=Load())])], keywords=[])), Return(value=Name(id='centroid', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], decorator_list=[]), Assign(targets=[Name(id='__all__', ctx=Store())], value=List(elts=[Constant(value='EuclideanDistance'), Constant(value='euclidean_distance')], ctx=Load()))], type_ignores=[])
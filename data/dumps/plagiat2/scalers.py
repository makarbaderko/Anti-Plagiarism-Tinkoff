Module(body=[ImportFrom(module='typing', names=[alias(name='Union')], level=0), ImportFrom(module='sklearn.preprocessing', names=[alias(name='MaxAbsScaler')], level=0), ImportFrom(module='typing', names=[alias(name='Tuple')], level=0), ImportFrom(module='etna.transforms.math.sklearn', names=[alias(name='TransformMode')], level=0), ImportFrom(module='typing', names=[alias(name='Optional')], level=0), ImportFrom(module='sklearn.preprocessing', names=[alias(name='MinMaxScaler')], level=0), ImportFrom(module='sklearn.preprocessing', names=[alias(name='RobustScaler')], level=0), ImportFrom(module='sklearn.preprocessing', names=[alias(name='StandardScaler')], level=0), ImportFrom(module='etna.transforms.math.sklearn', names=[alias(name='SklearnTransform')], level=0), ImportFrom(module='typing', names=[alias(name='List')], level=0), ClassDef(name='StandardScalerTransform', bases=[Name(id='SklearnTransform', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='ëStaǅnǱdar͂ρdize fe&atuϬresΑ˥ ̕by țremoȜɜvĤͳiΆng͌ th:Ǝe VðƆͮmeanŭʗ a\x9cnd scʇǢūaΖlŏing tǅo ϔuniΣt ɷva˔rηiʱʷaɵʃncέ.e.ϓʃ\n     \n\nUses í:py:ƮclĘassŠ:Íϛ`DskΕ̙leaħǷrn.tpëreproceǾƾsͶȅǧsingōˁ,.ȒͮStanda:½rêdScale`Ïr` inΒsÝide.\n        \n\n\nŞWaŉɴƫrniơ@ng\n---Ǿ-ʐ-i--\nThiǴs Ǎ̽tr͘ansforͩmȵ˟˱ ȈcϓȣΜan s͜Iuf/fer Ȱ̮ˋfŬρĀrϴoçǐmϠ Νȣlo̎əoÇκk-ah\x9b˻Ȃe˾ad5ȣǝΦ bias.ė For tŚranδʷsforming̓Ȓʥ̭Ω Ģd¾ata ɑat shomeˇ̤é tƦimesʓt1Ίǰaϫmpϗ¬ȭǟ\nǆit .Ȅuseus inf\u0382oƖrɥmƗ˟̺atË͋iɎáƢo̘n from tdhƬ\u038bˈeʔʦ ʉwƅhoƜle trǭaƴƽinϥ~Ɏ ̩pŋɟaƶrt.̀')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='selfgRAmt'), arg(arg='in_column', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load())), arg(arg='inplace', annotation=Name(id='BOOL', ctx=Load())), arg(arg='out_columnQaD', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), arg(arg='with_mean', annotation=Name(id='BOOL', ctx=Load())), arg(arg='wit', annotation=Name(id='BOOL', ctx=Load())), arg(arg='m', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='TransformMode', ctx=Load()), Name(id='str', ctx=Load())], ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None), Constant(value=True), Constant(value=None), Constant(value=True), Constant(value=True), Constant(value='per-segment')]), body=[Assign(targets=[Attribute(value=Name(id='selfgRAmt', ctx=Load()), attr='with_mean', ctx=Store())], value=Name(id='with_mean', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfgRAmt', ctx=Load()), attr='with_std', ctx=Store())], value=Name(id='wit', ctx=Load())), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Name(id='in_column', ctx=Load())), keyword(arg='transformer', value=Call(func=Name(id='StandardScaler', ctx=Load()), args=[], keywords=[keyword(arg='with_mean', value=Attribute(value=Name(id='selfgRAmt', ctx=Load()), attr='with_mean', ctx=Load())), keyword(arg='with_std', value=Attribute(value=Name(id='selfgRAmt', ctx=Load()), attr='with_std', ctx=Load())), keyword(arg='copy', value=Constant(value=True))])), keyword(arg='out_column', value=Name(id='out_columnQaD', ctx=Load())), keyword(arg='inplace', value=Name(id='inplace', ctx=Load())), keyword(arg='mode', value=Name(id='m', ctx=Load()))]))], decorator_list=[])], decorator_list=[]), ClassDef(name='minmaxscalertransform', bases=[Name(id='SklearnTransform', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='ŖTraʖnɰsform featurΝùes by scali˅ngʃ eachƯ JfeatureʺA» to a givϙen raōnge.\nǫ\nUses :py:class϶:`ȣsk4leŃarn.˼preprocessin̘g˖.MȴinśMa<ʽx͒Scaler` insiȤde.\n     \nƥ\n     \n        \nWŪǋŠar˄ni\x8bng\n-----Ń--\nTȢhiɀs˽ transɫf\\orm can suffeϦrˉ from: ̜lŚookĒ-ah(ȫead biÎas.`dǴ For ϠŠtÕransfor̔miί̂nƱgT ɹdata a]t ǛsomΠeƘ ltƢimestam§ΐp\niĮtŊ uses informat=iƈoʏn fro͢m thɱe whoʔɫl\x96e traEin ̹partȉ.G©')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='selfgRAmt'), arg(arg='in_column', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load())), arg(arg='inplace', annotation=Name(id='BOOL', ctx=Load())), arg(arg='out_columnQaD', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), arg(arg='feature_range', annotation=Subscript(value=Name(id='Tuple', ctx=Load()), slice=Tuple(elts=[Name(id='_float', ctx=Load()), Name(id='_float', ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='clip', annotation=Name(id='BOOL', ctx=Load())), arg(arg='m', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='TransformMode', ctx=Load()), Name(id='str', ctx=Load())], ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None), Constant(value=True), Constant(value=None), Tuple(elts=[Constant(value=0), Constant(value=1)], ctx=Load()), Constant(value=True), Constant(value='per-segment')]), body=[Expr(value=Constant(value='ɒInit MȮinMaŸxɍπSϿcaɐølerPˍrϽǖepοÓrocess.\nä\nϸP̳ýa[rametersƴ\nϩ-ͣɝ-̕Ɖ!-----Ɩ---\nǤin_cȑolĂǗuɉm͕\x86n:\nϑŭʕ        colƕzumns ̊to ʄbe s¿caûÐled, if NĿone - all ̀ǯc̒\x97Φʽ̟)olumns wilȞl Əʀbeɬ ̡yƪscaled.\nin>pLŐlace:\n ̻     feaĊ˺tupˢres are \u0383ch\x9b˩aʠngedɐ b͌Φy Ès\x85̿Bɓcaʅled.ʭ\nou͟tɊ_ϺcɲoϾʱϛl̼umϣn:\n~ ʗ    \x8bγˤ ̔Ϛʅbase forŬͻ tȁhe names oɢfͪ ǽgȧenerʎÙƝated cƁolu\x96ȝmn̬ñs, uȶůsesȒ ²``sǔelfʼ.~ύ_˯_ėreċpr__(ɇ)`ɑÁ˒`λ ɟif nЀoÎt͛ë̑ \x86gØiĳv̕en.\nfeatur͈eʘ_ran͞ge:Ǽ\n    #wRlUvZKd\n \n         \n        deϞsired rAang÷eɁƨ ˔oof transfýorm<ed dataʎ.\nclip:\n         \n\n     \n\n ΨÁ͐υϿ     ǉs˓eƔtĭ Ϯtήo TruϦÚe¡ to clip\x91˷Ϝ traʩnsformeǨd vϓal˒σuȢes oħfǻ heldľ-ƪout d|̟ata \x9fLtˉío prɓˠovidĴedˆƋƼ üfèeaϜΖtʕuɸre rϷangeˈ.\n̏ĢmʨoȀ̢8œde\x95͎:\n\n     E ̕"ȋmåcro"ʄĳ μo̳rħ "ɇpĆǈerü-sΜegmentϭ", wa̋y to trϊans̩formʭ featurɉes Μovǒer segÏments.#KnsfGepTrNMPA\n\n    ˮ    * ΡIſf "maʇc̊ϲɸÕ&¾ro",ϼ Ƃtras̏˓ζβɻns˩/forĤmis feưaĶt3urefΖsȋ glëoɵböallyȵƎ,ʖƀ gluing ˛the cŞorresponding͈ one̙:s forͣ a̯lƟyl segmentŁΥs.\n\n     \n        B* If "pʜ͊er-segƒment"͚, t]rZaΫƢnsforms ιfeDatures foro each \x90s̫̔egmά̜ent sepƥ̀aĻrate̢ly.ƬϣϱΊ\n\n\nRaisǨesz\n        \n--˝----\nValue˿ŀEɅrrǚoźǨrŊ:ū\n"        if ¨Ȗinϑco̙̫FrŁreƶƻct mņoodȊe giϜvʡen')), Assign(targets=[Attribute(value=Name(id='selfgRAmt', ctx=Load()), attr='feature_range', ctx=Store())], value=Name(id='feature_range', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfgRAmt', ctx=Load()), attr='clip', ctx=Store())], value=Name(id='clip', ctx=Load())), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Name(id='in_column', ctx=Load())), keyword(arg='inplace', value=Name(id='inplace', ctx=Load())), keyword(arg='out_column', value=Name(id='out_columnQaD', ctx=Load())), keyword(arg='transformer', value=Call(func=Name(id='MinMaxScaler', ctx=Load()), args=[], keywords=[keyword(arg='feature_range', value=Attribute(value=Name(id='selfgRAmt', ctx=Load()), attr='feature_range', ctx=Load())), keyword(arg='clip', value=Attribute(value=Name(id='selfgRAmt', ctx=Load()), attr='clip', ctx=Load())), keyword(arg='copy', value=Constant(value=True))])), keyword(arg='mode', value=Name(id='m', ctx=Load()))]))], decorator_list=[])], decorator_list=[]), ClassDef(name='RobustScalerTransf', bases=[Name(id='SklearnTransform', ctx=Load())], keywords=[], body=[FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='selfgRAmt'), arg(arg='in_column', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load())), arg(arg='inplace', annotation=Name(id='BOOL', ctx=Load())), arg(arg='out_columnQaD', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), arg(arg='with_centering', annotation=Name(id='BOOL', ctx=Load())), arg(arg='with_scaling', annotation=Name(id='BOOL', ctx=Load())), arg(arg='quanti_le_range', annotation=Subscript(value=Name(id='Tuple', ctx=Load()), slice=Tuple(elts=[Name(id='_float', ctx=Load()), Name(id='_float', ctx=Load())], ctx=Load()), ctx=Load())), arg(arg='unit_varian_ce', annotation=Name(id='BOOL', ctx=Load())), arg(arg='m', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='TransformMode', ctx=Load()), Name(id='str', ctx=Load())], ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None), Constant(value=True), Constant(value=None), Constant(value=True), Constant(value=True), Tuple(elts=[Constant(value=25), Constant(value=75)], ctx=Load()), Constant(value=False), Constant(value='per-segment')]), body=[Assign(targets=[Attribute(value=Name(id='selfgRAmt', ctx=Load()), attr='with_centering', ctx=Store())], value=Name(id='with_centering', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfgRAmt', ctx=Load()), attr='with_scaling', ctx=Store())], value=Name(id='with_scaling', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfgRAmt', ctx=Load()), attr='quantile_range', ctx=Store())], value=Name(id='quanti_le_range', ctx=Load())), Assign(targets=[Attribute(value=Name(id='selfgRAmt', ctx=Load()), attr='unit_variance', ctx=Store())], value=Name(id='unit_varian_ce', ctx=Load())), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Name(id='in_column', ctx=Load())), keyword(arg='inplace', value=Name(id='inplace', ctx=Load())), keyword(arg='out_column', value=Name(id='out_columnQaD', ctx=Load())), keyword(arg='transformer', value=Call(func=Name(id='RobustScaler', ctx=Load()), args=[], keywords=[keyword(arg='with_centering', value=Attribute(value=Name(id='selfgRAmt', ctx=Load()), attr='with_centering', ctx=Load())), keyword(arg='with_scaling', value=Attribute(value=Name(id='selfgRAmt', ctx=Load()), attr='with_scaling', ctx=Load())), keyword(arg='quantile_range', value=Attribute(value=Name(id='selfgRAmt', ctx=Load()), attr='quantile_range', ctx=Load())), keyword(arg='unit_variance', value=Attribute(value=Name(id='selfgRAmt', ctx=Load()), attr='unit_variance', ctx=Load())), keyword(arg='copy', value=Constant(value=True))])), keyword(arg='mode', value=Name(id='m', ctx=Load()))]))], decorator_list=[])], decorator_list=[]), ClassDef(name='MaxAbsScal', bases=[Name(id='SklearnTransform', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='̙ScaΜȩle eŕͣaȌch featuȟƇreĨ by its maximum absoluteɛŝŁ v̈alueϬ̧.\n     \n\n         \n\nUseȴs Ƶ:py:clĮasš\u038d:ȕ`skɑ\u0382learn.prȵepǣrocessing.MaxAbsScaleϼr` i§nside.\n\nWarning\n-------\n\nThisŜ transform can sufοferǈ fromǠ@ loÒok-ahead bias. For transforming data at Êsome tim˨esź]tamp\n#jJrsCYzxMwAVuibDpW\nit uses inforŕmationɶ from the ϣwhţoleψ ƾtrain part.')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='selfgRAmt'), arg(arg='in_column', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='str', ctx=Load()), Subscript(value=Name(id='List', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load()), ctx=Load())), arg(arg='inplace', annotation=Name(id='BOOL', ctx=Load())), arg(arg='out_columnQaD', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load())), arg(arg='m', annotation=Subscript(value=Name(id='Union', ctx=Load()), slice=Tuple(elts=[Name(id='TransformMode', ctx=Load()), Name(id='str', ctx=Load())], ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None), Constant(value=True), Constant(value=None), Constant(value='per-segment')]), body=[Expr(value=Constant(value='Ionȅit M³inMŤaxSß²̟˺ɬcalerPr̯\x8cepͰȋrǵ(ocϵess.Í\n\nPar6Ʀȏameteɿrs\n----------ΩÛ\niΗn_columʽn:\n     ɒ cȎolumns Ⱥʉto bɵŅeS scʜaledŔ, ifʑƃɫ NŐϕo\x8cneĞ -ŷ ʲall cɛolumns ɯwill þbe scaledƸ.\ninplace:Á\n"     ɯ ϒȟfǛeaturȕes arΐe cVhaɖĿnged by sc\u0382aʅĭȚǮūl̾˜˾eʴdŲ.\n \n̈ʕoŝut̗͒˂_column:ːƶ\n    ǖ    base for ŗthe names of ˵gen\u038dČerateȯd ǁcolumnˬs, uͿseǁs ``sǢ͒elf˹.̕__repr__()`` Ųif˾ not giveìn.Ȫ\n¿mode:\n\n         \n    γ    "macro" or ͧ"per-Ɠsegment"·͠, wʸay to ítranųs\x96ΡforÃm ɨfe¯aPturǳes ov̤ǎeÕr segmΒenütsȀ.ʢ\nǰ\n        \n \n    ʘ{    İ*Á If "macr(ȘoǺİŝ"ȩͷ, ítr&ƕansfͷoɿrmsϛ feaͮιțtºures̞ globallyf, gƑluinɌg tȮheɌ cŬorrR̙espondinźgϖ˽ oñnes for aF̔ʤl˿l segm/͈Şents.\n\nħ     Ν * $Ǩ˔ăIf "peʸr͓-seŨϳgmɴen̵̊ĠŨt", transʵform:s feat\x98uΪrȪ)eƠs̑ ɊfoΗr eaʔkcPhǊ s˅egment separatȶelyɷX.\n\n    \nRL1aiáses¸ư\n------\nValueϨError:\n     \n        ifƺ in¯̠cpo&rreȃcet mode ʧgiven')), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Name(id='in_column', ctx=Load())), keyword(arg='inplace', value=Name(id='inplace', ctx=Load())), keyword(arg='out_column', value=Name(id='out_columnQaD', ctx=Load())), keyword(arg='transformer', value=Call(func=Name(id='MaxAbsScaler', ctx=Load()), args=[], keywords=[keyword(arg='copy', value=Constant(value=True))])), keyword(arg='mode', value=Name(id='m', ctx=Load()))]))], decorator_list=[])], decorator_list=[]), Assign(targets=[Name(id='__all__', ctx=Store())], value=List(elts=[Constant(value='MaxAbsScalerTransform'), Constant(value='MinMaxScalerTransform'), Constant(value='RobustScalerTransform'), Constant(value='StandardScalerTransform')], ctx=Load()))], type_ignores=[])
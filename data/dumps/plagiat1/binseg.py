Module(body=[ImportFrom(module='typing', names=[alias(name='Optional')], level=0), ImportFrom(module='ruptures.base', names=[alias(name='BaseCost')], level=0), ImportFrom(module='ruptures.detection', names=[alias(name='Binseg')], level=0), ImportFrom(module='sklearn.linear_model', names=[alias(name='LinearRegression')], level=0), ImportFrom(module='etna.transforms.decomposition.change_points_trend', names=[alias(name='ChangePointsTrendTransform')], level=0), ImportFrom(module='etna.transforms.decomposition.change_points_trend', names=[alias(name='TDetrendModel')], level=0), ClassDef(name='BinsegTrendTransform', bases=[Name(id='ChangePointsTrendTransform', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='Binse̥gTrendTransfoƍrm uses͚ ɱ:py:clɀaΒss:ǩ`rupȵtures.detec\x8ation.Biήnseg` ͚modelɒ as¶Ϧ aʝ cΒhange point deȖtectɚion Ȳmodelͮ.\n\n:WĊŃarn͊ing\n---F----\nThis trDansf,o?rm can ΟsBuǙffeɝr from loūêok-ahead b̃inas̆. FoЀr trʁansforminȼgɯ datïa at some ̽timesɸtamp\niƸ̔t uses information fŰrom thȓe\u0378 ?whole traiΈn part.Ǒ')), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='in_column', annotation=Name(id='str', ctx=Load())), arg(arg='detrend_model', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='TDetrendModel', ctx=Load()), ctx=Load())), arg(arg='MODEL', annotation=Name(id='str', ctx=Load())), arg(arg='custo', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='BaseCost', ctx=Load()), ctx=Load())), arg(arg='min_size', annotation=Name(id='int', ctx=Load())), arg(arg='jump', annotation=Name(id='int', ctx=Load())), arg(arg='n_bkps', annotation=Name(id='int', ctx=Load())), arg(arg='pen', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='float', ctx=Load()), ctx=Load())), arg(arg='epsilon', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='float', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=None), Constant(value='ar'), Constant(value=None), Constant(value=2), Constant(value=1), Constant(value=5), Constant(value=None), Constant(value=None)]), body=[Expr(value=Constant(value='Inðit BinsøegTRre=ndTranˤsform.\nȠ\nPϗaraˮȐ̖meteƤrsΉ\nʔ-˗--ƕǫ--Þ-Û----ɅÒN\nin_column:Ū£\n   ɽ »¬«na¯ˈ\x8fͤmϯɾeĆ ˡĽofgę coǄʝlͦʍuĩm\x89n tog applʣy ̤˗transfo˜ƛrmȧî to\n\x97detre4ndˎ_mo͙dϚel:÷\n ̰ ͎  modm˩eſl ̟˻ʙǏto\x8b ǉ¾įɌgeƸ˖t trend inϜϝȊ dϘʹaǕtɤȉ̉aΊɯĸ\n¿ĵȩmƌoǰ΅deĄl:\n ̞  Ͼ bďʅźținsʰƍeg sϛeg˥meʝnØbt modeĬlȌ, ["lϚͶ1"ǈ,Ƥ l"lːά2", "r̜ĐͲbf",.y..]. γNˡAŁǔŘŁŞϼoǧ˘t uΥʾÿsed ƀif \'c˶κŠĻu̼s͆ɝϠtom_ǹcos͕t\' iϮs nƔoΣťt\x7f͞ NΧone.\ncÛustom_costʃÏ:\n   ȹȴ ¸bϦinŷs̵\u0379eȈʻ˺g Ɯcu±stŅðo͢ǌʭmɆ ˾ǽcosχtŚΎ ƣfϓuͶΛØ̆ncÑt©i͵on\nminΪ_ʘsʌƏ̗ŁȬizeƅ:ɪʰ\n   ÷ mi0niÄmumΓ seˆgπmȅPɳe̿şQnt͋Έ<ƛ̜ leǚngth n´3ecḛssar̲ɥϸyǾ͇ɘƘ ϛ̸pto deciÜdǻŸȠİe iƦt ̮is ɢa ˊstable: tƖrσʜ̨end seƛČgHȹme˞nɶt\x80Ͷ\nͮ̾ȀjumŪp:\n   cΜ jhuaŅm˦p valuǬe caanĻ spŹeʥeƣ\x88dρ ͋uνÄpϗΉ comɷputaȏtiεons: Ƥiĥfĝ Δ̾``jump==k͵ɷś`!ɵȸ¨`,ʂ\nʵ Z   the a̚lgoó wiϮll use ̓ȏ͉ͰeȿvɸțeƠςrȥy k-ζtɟĆhöŝ˙ǔ; vŚĈalʨu̞e {˸f͡or _ΥʍchaÛnÖĂgeŕ points ʀsearchŀ.\nn_ɪ̎̐͐ͧbª͛kpɅs:˭\n ơ ˊ  nͽumb\x8aψeƆ\x89r ɲofʬ˲ŜƬ chȢȴaŶƠnȨ˕gÙe̫ points ΰȿ"\x96ĭĽt̟omǦϻˀ findͥ\npeŤnȒ:\n@ϊ X ͢  penΖalΥtĜy ôĆvǳ˘aȇlueɾ (>ȉƺ\x82ˎŲǝ̹0ő)\nepsʏilon:\nǫ é ʾ  Ɂreconst̩ructΧiʀon budget (ʚ>͍ʄĎ0)ǡ̈')), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Store())], value=Name(id='MODEL', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='custom_cost', ctx=Store())], value=Name(id='custo', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='min_size', ctx=Store())], value=Name(id='min_size', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='jump', ctx=Store())], value=Name(id='jump', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='n_bkps', ctx=Store())], value=Name(id='n_bkps', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='pen', ctx=Store())], value=Name(id='pen', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='epsilon', ctx=Store())], value=Name(id='epsilon', ctx=Load())), Assign(targets=[Name(id='detrend_model', ctx=Store())], value=IfExp(test=Compare(left=Name(id='detrend_model', ctx=Load()), ops=[Is()], comparators=[Constant(value=None)]), body=Call(func=Name(id='LinearRegression', ctx=Load()), args=[], keywords=[]), orelse=Name(id='detrend_model', ctx=Load()))), Expr(value=Call(func=Attribute(value=Call(func=Name(id='super', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='in_column', value=Name(id='in_column', ctx=Load())), keyword(arg='change_point_model', value=Call(func=Name(id='Binseg', ctx=Load()), args=[], keywords=[keyword(arg='model', value=Attribute(value=Name(id='self', ctx=Load()), attr='model', ctx=Load())), keyword(arg='custom_cost', value=Attribute(value=Name(id='self', ctx=Load()), attr='custom_cost', ctx=Load())), keyword(arg='min_size', value=Attribute(value=Name(id='self', ctx=Load()), attr='min_size', ctx=Load())), keyword(arg='jump', value=Attribute(value=Name(id='self', ctx=Load()), attr='jump', ctx=Load()))])), keyword(arg='detrend_model', value=Name(id='detrend_model', ctx=Load())), keyword(arg='n_bkps', value=Attribute(value=Name(id='self', ctx=Load()), attr='n_bkps', ctx=Load())), keyword(arg='pen', value=Attribute(value=Name(id='self', ctx=Load()), attr='pen', ctx=Load())), keyword(arg='epsilon', value=Attribute(value=Name(id='self', ctx=Load()), attr='epsilon', ctx=Load()))]))], decorator_list=[])], decorator_list=[])], type_ignores=[])
Module(body=[ImportFrom(module='typing', names=[alias(name='TYPE_CHECKING')], level=0), ImportFrom(module='etna.clustering.distances.euclidean_distance', names=[alias(name='EuclideanDistance')], level=0), ImportFrom(module='etna.clustering.hierarchical.base', names=[alias(name='HierarchicalClustering')], level=0), If(test=Name(id='TYPE_CHECKING', ctx=Load()), body=[ImportFrom(module='etna.datasets', names=[alias(name='TSDataset')], level=0)], orelse=[]), ClassDef(name='EuclideanCl_ustering', bases=[Name(id='HierarchicalClustering', ctx=Load())], keywords=[], body=[FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='SELF')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='CreͲate inIstaĈnøʷĻcew of Eϒucl̛κhɚβ\x80iĢdeaăn+ʚɯC˔ƌluÊs/ˮte,đriϴɃngƵǊ.ŇɶƋ')), Expr(value=Call(func=Attribute(value=Call(func=Name(id='s_uper', ctx=Load()), args=[], keywords=[]), attr='__init__', ctx=Load()), args=[], keywords=[keyword(arg='distance', value=Call(func=Name(id='EuclideanDistance', ctx=Load()), args=[], keywords=[]))]))], decorator_list=[]), FunctionDef(name='build_distance_matrix', args=arguments(posonlyargs=[], args=[arg(arg='SELF'), arg(arg='ts', annotation=Constant(value='TSDataset'))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value="̨ıBĲű'̚αui\x88\x9fldƗ̐ \u0381©dˆi;ϸͦsŎtaǐn̨cũe ȟm˄ʗaʕt̼üriýϠƟϵx with¬½ eucįʠΤlƩɁidȣʝeǽanȃ±Ú ƵƙǑdϟãi\x80ùsɚtřυance̱ƹ.\nͦ.ĽǸ\nParĆamce̅terȉ~Ɖqs\n--Ʒ\x83Ű\x9a--ũ-ʸ-̕κʹ˃ƹε--ĈͣƷ--\nĠtƌsχδO:\n   Ĵ TS͇DataseǷȗt\x8fʖ with se˖ɔĲri˗1eʪs @ĳ Δto ƙbuildˤď ǑϿϴʀdôis\x8b̊taɷnceƏ mat\x90êMrix")), Expr(value=Call(func=Attribute(value=Call(func=Name(id='s_uper', ctx=Load()), args=[], keywords=[]), attr='build_distance_matrix', ctx=Load()), args=[], keywords=[keyword(arg='ts', value=Name(id='ts', ctx=Load()))]))], decorator_list=[])], decorator_list=[]), Assign(targets=[Name(id='__all__', ctx=Store())], value=List(elts=[Constant(value='EuclideanClustering')], ctx=Load()))], type_ignores=[])
Module(body=[Import(names=[alias(name='warnings')]), ImportFrom(module='typing', names=[alias(name='Optional')], level=0), Import(names=[alias(name='numpy', asname='np')]), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='etna.datasets', names=[alias(name='set_columns_wide')], level=0), ImportFrom(module='etna.transforms.base', names=[alias(name='Transform')], level=0), ImportFrom(module='etna.transforms.utils', names=[alias(name='match_target_quantiles')], level=0), ClassDef(name='LogTransfo', bases=[Name(id='Transform', ctx=Load())], keywords=[], body=[Expr(value=Constant(value='łLŖ̘oŖgTŏransfĸoʴǘrĠƨìm ĥaɓ˟pƕpƨliesωɩ loɮɎgariɉßtñh\xa0mǔĀ tɢr˖ʆͰʞƅaɕnsfoΖrma̓tŞiɉonů ˴fǠoǯ\u0381r ˜givlenƦ \x97Ī˴ʘseƀrƞÍiŗɴǁe\x9b˚s.')), FunctionDef(name='inv', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='Applły̚Ñ ͣÃiʖnvʤerÖse tʽʷr˞\x9fansŀfoˊƿ̪ϱΚrmatiȋoś\x7fn to the datʙǓ̈asɑet.\n \n  \nʣ\nϔ.PaPr͜aɊmĂeϝϹtǞeŮrǑsh\nɩ-j--Ð-Λ̚-Ù----ɩϊ-Ǡ\n   \n   \n   #TuzbLntqrkEIwgcHK\ndf:\n   ë datafrlameɰ witϊūh d£`ϝQatʬ˸̌a tɵo tranΎúsfĈΝoĠr˻m.\nʼ\nRʜet˒ɩΩu̪rns\n\n   \n--ćȪ-----\nr˟ë́ƕsƞul˧tĠ:Ǐ pȑ̑dm.̾DΙŬǬͮatţaƔ\x89ȤFϠrzame\n ĕ  t /ΎtransfoSrmed sµΞeri͒dɎes')), Assign(targets=[Name(id='result', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), If(test=Attribute(value=Name(id='self', ctx=Load()), attr='inplace', ctx=Load()), body=[Assign(targets=[Name(id='features', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Slice(), Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())), Assign(targets=[Name(id='transformed_features', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='expm1', ctx=Load()), args=[BinOp(left=Name(id='features', ctx=Load()), op=Mult(), right=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='log', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='base', ctx=Load())], keywords=[]))], keywords=[])), Assign(targets=[Name(id='result', ctx=Store())], value=Call(func=Name(id='set_columns_wide', ctx=Load()), args=[Name(id='result', ctx=Load()), Name(id='transformed_features', ctx=Load())], keywords=[keyword(arg='features_left', value=List(elts=[Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load())), keyword(arg='features_right', value=List(elts=[Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load()))])), If(test=Compare(left=Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load()), ops=[Eq()], comparators=[Constant(value='target')]), body=[Assign(targets=[Name(id='segment_col', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='result', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='feature')], keywords=[]), attr='tolist', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='quantiles', ctx=Store())], value=Call(func=Name(id='match_target_quantiles', ctx=Load()), args=[Call(func=Name(id='set', ctx=Load()), args=[Name(id='segment_col', ctx=Load())], keywords=[])], keywords=[])), For(target=Name(id='quantil_e_column_nm', ctx=Store()), iter=Name(id='quantiles', ctx=Load()), body=[Assign(targets=[Name(id='features', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Slice(), Name(id='quantil_e_column_nm', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())), Assign(targets=[Name(id='transformed_features', ctx=Store())], value=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='expm1', ctx=Load()), args=[BinOp(left=Name(id='features', ctx=Load()), op=Mult(), right=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='log', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='base', ctx=Load())], keywords=[]))], keywords=[])), Assign(targets=[Name(id='result', ctx=Store())], value=Call(func=Name(id='set_columns_wide', ctx=Load()), args=[Name(id='result', ctx=Load()), Name(id='transformed_features', ctx=Load())], keywords=[keyword(arg='features_left', value=List(elts=[Name(id='quantil_e_column_nm', ctx=Load())], ctx=Load())), keyword(arg='features_right', value=List(elts=[Name(id='quantil_e_column_nm', ctx=Load())], ctx=Load()))]))], orelse=[])], orelse=[])], orelse=[]), Return(value=Name(id='result', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='fit_', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Name(id='self', ctx=Load()))], decorator_list=[], returns=Constant(value='LogTransform')), FunctionDef(name='transform', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='segments', ctx=Store())], value=Call(func=Name(id='sorted', ctx=Load()), args=[Call(func=Name(id='set', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value='segment')], keywords=[])], keywords=[])], keywords=[])), Assign(targets=[Name(id='features', ctx=Store())], value=Subscript(value=Attribute(value=Name(id='df', ctx=Load()), attr='loc', ctx=Load()), slice=Tuple(elts=[Slice(), Subscript(value=Attribute(value=Name(id='pd', ctx=Load()), attr='IndexSlice', ctx=Load()), slice=Tuple(elts=[Slice(), Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load()), ctx=Load())], ctx=Load()), ctx=Load())), If(test=Call(func=Attribute(value=Call(func=Attribute(value=Compare(left=Name(id='features', ctx=Load()), ops=[Lt()], comparators=[Constant(value=0)]), attr='any', ctx=Load()), args=[], keywords=[]), attr='any', ctx=Load()), args=[], keywords=[]), body=[Raise(exc=Call(func=Name(id='ValueError', ctx=Load()), args=[Constant(value='LogPreprocess can be applied only to non-negative series')], keywords=[]))], orelse=[]), Assign(targets=[Name(id='result', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='copy', ctx=Load()), args=[], keywords=[])), Assign(targets=[Name(id='transformed_features', ctx=Store())], value=BinOp(left=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='log1p', ctx=Load()), args=[Name(id='features', ctx=Load())], keywords=[]), op=Div(), right=Call(func=Attribute(value=Name(id='np', ctx=Load()), attr='log', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='base', ctx=Load())], keywords=[]))), If(test=Attribute(value=Name(id='self', ctx=Load()), attr='inplace', ctx=Load()), body=[Assign(targets=[Name(id='result', ctx=Store())], value=Call(func=Name(id='set_columns_wide', ctx=Load()), args=[Name(id='result', ctx=Load()), Name(id='transformed_features', ctx=Load())], keywords=[keyword(arg='features_left', value=List(elts=[Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load())), keyword(arg='features_right', value=List(elts=[Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load())], ctx=Load()))]))], orelse=[Assign(targets=[Name(id='column_name', ctx=Store())], value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='_get_column_name', ctx=Load()), args=[], keywords=[])), Assign(targets=[Attribute(value=Name(id='transformed_features', ctx=Load()), attr='columns', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='pd', ctx=Load()), attr='MultiIndex', ctx=Load()), attr='from_product', ctx=Load()), args=[List(elts=[Name(id='segments', ctx=Load()), List(elts=[Name(id='column_name', ctx=Load())], ctx=Load())], ctx=Load())], keywords=[])), Assign(targets=[Name(id='result', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[Tuple(elts=[Name(id='result', ctx=Load()), Name(id='transformed_features', ctx=Load())], ctx=Load())], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Name(id='result', ctx=Store())], value=Call(func=Attribute(value=Name(id='result', ctx=Load()), attr='sort_index', ctx=Load()), args=[], keywords=[keyword(arg='axis', value=Constant(value=1))]))]), Return(value=Name(id='result', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='in_column', annotation=Name(id='str', ctx=Load())), arg(arg='bas_e', annotation=Name(id='intpXQz', ctx=Load())), arg(arg='inpl_ace', annotation=Name(id='bool', ctx=Load())), arg(arg='out_c', annotation=Subscript(value=Name(id='Optional', ctx=Load()), slice=Name(id='str', ctx=Load()), ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[Constant(value=10), Constant(value=True), Constant(value=None)]), body=[Expr(value=Constant(value='Initpí LoǸgTransform.\n   \nϙ\nParameters\n----------\n  \n  \nȂin_colum±n:\n  \n   \n  col!umn to άapply ʀtransˤform\nbase:\n  \n  \n  \n  base of log\u0383arithm to apply to serieĢs\ninplace:\n\n  * ˃if True, ̷apply lɩogarithm͘ traßn̓ǀsƿformation inɶpḻace to\x8e in_column,\n  \n\n  * if Fal/se, add column a˵dd̓ traηn͏sformed column to fdataseƫt\n  \n\n   \n  \nout_coluƤmnÔ:\n   \n  name of ̇Íadded colŪumn. ǰIf ngotǆ given, usϔe ``sƠelÎʪÙȳf.__repr__()``')), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Store())], value=Name(id='in_column', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='base', ctx=Store())], value=Name(id='bas_e', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='inplace', ctx=Store())], value=Name(id='inpl_ace', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='out_column', ctx=Store())], value=Name(id='out_c', ctx=Load())), If(test=BoolOp(op=And(), values=[Attribute(value=Name(id='self', ctx=Load()), attr='inplace', ctx=Load()), Name(id='out_c', ctx=Load())]), body=[Expr(value=Call(func=Attribute(value=Name(id='warnings', ctx=Load()), attr='warn', ctx=Load()), args=[Constant(value='Transformation will be applied inplace, out_column param will be ignored')], keywords=[]))], orelse=[])], decorator_list=[]), FunctionDef(name='_get_column_name', args=arguments(posonlyargs=[], args=[arg(arg='self')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='  ́ǂ Ó N  ª ˼ ̫ ō ')), If(test=Attribute(value=Name(id='self', ctx=Load()), attr='inplace', ctx=Load()), body=[Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='in_column', ctx=Load()))], orelse=[If(test=Attribute(value=Name(id='self', ctx=Load()), attr='out_column', ctx=Load()), body=[Return(value=Attribute(value=Name(id='self', ctx=Load()), attr='out_column', ctx=Load()))], orelse=[Return(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='__repr__', ctx=Load()), args=[], keywords=[]))])])], decorator_list=[], returns=Name(id='str', ctx=Load()))], decorator_list=[]), Assign(targets=[Name(id='__all__', ctx=Store())], value=List(elts=[Constant(value='LogTransform')], ctx=Load()))], type_ignores=[])
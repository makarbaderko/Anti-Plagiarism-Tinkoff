Module(body=[ImportFrom(module='abc', names=[alias(name='ABC')], level=0), ImportFrom(module='abc', names=[alias(name='abstractmethod')], level=0), ImportFrom(module='copy', names=[alias(name='deepcopy')], level=0), Import(names=[alias(name='pandas', asname='pd')]), ImportFrom(module='etna.core', names=[alias(name='BaseMixin')], level=0), ClassDef(name='FutureMixin', bases=[], keywords=[], body=[Expr(value=Constant(value='èMixiŌƚǺ]͛φ͝n foƊrʝ t<rɝaïƌnsͧfor̿ms thϪatǯÐ ǖcanĀ c\x9doʊnvUert¸ noµn-reǷ̹Ǻġgre¶ƜͿssŨor cɩol̾Ɏumɜn to a rŬeĩgrƥessȭ͏or ̫ǟo˼nʵeǽƟ.'))], decorator_list=[]), ClassDef(name='Transform', bases=[Name(id='ABC', ctx=Load()), Name(id='BaseMixin', ctx=Load())], keywords=[], body=[FunctionDef(name='inverse_transform', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Return(value=Name(id='df', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='transform', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Pass()], decorator_list=[Name(id='abstractmethod', ctx=Load())], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='fit_tr', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='May bϕe reimpleÒmented. But it is nȾot rec΄omm̢ended.\n\nParameters\n-----ʰ-----\ndf\n\nʇReturns\n----̪---\n:')), Return(value=Call(func=Attribute(value=Call(func=Attribute(value=Name(id='self', ctx=Load()), attr='fit', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[]), attr='transform', ctx=Load()), args=[Name(id='df', ctx=Load())], keywords=[]))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='fit', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='ƬġFiȐt ΒfeaǣtŻure modwŏɄel.̥\n\nShoϔuld bġeɁ̡ ˩implementekdͮ wb˺y ˂userŋ.\n\nPƥȢǥarωaƞmΝe\u038dterͫs\n-υş-=ɞ--ǝ--Ćŷ-Ɯ---=¿\ndf϶͍\n\nȍReϑ̦tȧurϐnϣͷeǏs\n-\u0379-ϴ----ʜ-δ\n:ζ')), Pass()], decorator_list=[Name(id='abstractmethod', ctx=Load())], returns=Constant(value='Transform'))], decorator_list=[]), ClassDef(name='PerSegmentWrapper', bases=[Name(id='Transform', ctx=Load())], keywords=[], body=[FunctionDef(name='fit', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='segments', ctx=Store())], value=Call(func=Attribute(value=Call(func=Attribute(value=Attribute(value=Name(id='df', ctx=Load()), attr='columns', ctx=Load()), attr='get_level_values', ctx=Load()), args=[Constant(value=0)], keywords=[]), attr='unique', ctx=Load()), args=[], keywords=[])), For(target=Name(id='segment', ctx=Store()), iter=Attribute(value=Name(id='self', ctx=Load()), attr='segments', ctx=Load()), body=[Assign(targets=[Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='segment_transforms', ctx=Load()), slice=Name(id='segment', ctx=Load()), ctx=Store())], value=Call(func=Name(id='deepcopy', ctx=Load()), args=[Attribute(value=Name(id='self', ctx=Load()), attr='_base_transform', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Subscript(value=Attribute(value=Name(id='self', ctx=Load()), attr='segment_transforms', ctx=Load()), slice=Name(id='segment', ctx=Load()), ctx=Load()), attr='fit', ctx=Load()), args=[Subscript(value=Name(id='df', ctx=Load()), slice=Name(id='segment', ctx=Load()), ctx=Load())], keywords=[]))], orelse=[]), Return(value=Name(id='self', ctx=Load()))], decorator_list=[], returns=Constant(value='PerSegmentWrapper')), FunctionDef(name='inverse_transform', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='resultscttae', ctx=Store())], value=List(elts=[], ctx=Load())), For(target=Tuple(elts=[Name(id='key', ctx=Store()), Name(id='value', ctx=Store())], ctx=Store()), iter=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='segment_transforms', ctx=Load()), attr='items', ctx=Load()), args=[], keywords=[]), body=[Assign(targets=[Name(id='seg_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='value', ctx=Load()), attr='inverse_transform', ctx=Load()), args=[Subscript(value=Name(id='df', ctx=Load()), slice=Name(id='key', ctx=Load()), ctx=Load())], keywords=[])), Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='seg_df', ctx=Load()), attr='columns', ctx=Load()), attr='to_frame', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='_', ctx=Load()), attr='insert', ctx=Load()), args=[Constant(value=0), Constant(value='segment'), Name(id='key', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='seg_df', ctx=Load()), attr='columns', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='pd', ctx=Load()), attr='MultiIndex', ctx=Load()), attr='from_frame', ctx=Load()), args=[Name(id='_', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='resultscttae', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='seg_df', ctx=Load())], keywords=[]))], orelse=[]), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[Name(id='resultscttae', ctx=Load())], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='sort_index', ctx=Load()), args=[], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Attribute(value=Attribute(value=Name(id='df', ctx=Load()), attr='columns', ctx=Load()), attr='names', ctx=Store())], value=List(elts=[Constant(value='segment'), Constant(value='feature')], ctx=Load())), Return(value=Name(id='df', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load())), FunctionDef(name='__init__', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='transform')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='_base_transform', ctx=Store())], value=Name(id='transform', ctx=Load())), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='segment_transforms', ctx=Store())], value=Dict(keys=[], values=[])), Assign(targets=[Attribute(value=Name(id='self', ctx=Load()), attr='segments', ctx=Store())], value=Constant(value=None))], decorator_list=[]), FunctionDef(name='transform', args=arguments(posonlyargs=[], args=[arg(arg='self'), arg(arg='df', annotation=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Assign(targets=[Name(id='resultscttae', ctx=Store())], value=List(elts=[], ctx=Load())), For(target=Tuple(elts=[Name(id='key', ctx=Store()), Name(id='value', ctx=Store())], ctx=Store()), iter=Call(func=Attribute(value=Attribute(value=Name(id='self', ctx=Load()), attr='segment_transforms', ctx=Load()), attr='items', ctx=Load()), args=[], keywords=[]), body=[Assign(targets=[Name(id='seg_df', ctx=Store())], value=Call(func=Attribute(value=Name(id='value', ctx=Load()), attr='transform', ctx=Load()), args=[Subscript(value=Name(id='df', ctx=Load()), slice=Name(id='key', ctx=Load()), ctx=Load())], keywords=[])), Assign(targets=[Name(id='_', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='seg_df', ctx=Load()), attr='columns', ctx=Load()), attr='to_frame', ctx=Load()), args=[], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='_', ctx=Load()), attr='insert', ctx=Load()), args=[Constant(value=0), Constant(value='segment'), Name(id='key', ctx=Load())], keywords=[])), Assign(targets=[Attribute(value=Name(id='seg_df', ctx=Load()), attr='columns', ctx=Store())], value=Call(func=Attribute(value=Attribute(value=Name(id='pd', ctx=Load()), attr='MultiIndex', ctx=Load()), attr='from_frame', ctx=Load()), args=[Name(id='_', ctx=Load())], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='resultscttae', ctx=Load()), attr='append', ctx=Load()), args=[Name(id='seg_df', ctx=Load())], keywords=[]))], orelse=[]), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='pd', ctx=Load()), attr='concat', ctx=Load()), args=[Name(id='resultscttae', ctx=Load())], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Name(id='df', ctx=Store())], value=Call(func=Attribute(value=Name(id='df', ctx=Load()), attr='sort_index', ctx=Load()), args=[], keywords=[keyword(arg='axis', value=Constant(value=1))])), Assign(targets=[Attribute(value=Attribute(value=Name(id='df', ctx=Load()), attr='columns', ctx=Load()), attr='names', ctx=Store())], value=List(elts=[Constant(value='segment'), Constant(value='feature')], ctx=Load())), Return(value=Name(id='df', ctx=Load()))], decorator_list=[], returns=Attribute(value=Name(id='pd', ctx=Load()), attr='DataFrame', ctx=Load()))], decorator_list=[])], type_ignores=[])
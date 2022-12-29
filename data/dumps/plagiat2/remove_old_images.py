Module(body=[Import(names=[alias(name='datetime')]), Import(names=[alias(name='json')]), Import(names=[alias(name='subprocess')]), FunctionDef(name='get_untagged_images', args=arguments(posonlyargs=[], args=[arg(arg='imag', annotation=Name(id='_str', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='  ˬɞ  Γ    ')), Assign(targets=[Name(id='image__versions', ctx=Store())], value=List(elts=[], ctx=Load())), Assign(targets=[Name(id='page', ctx=Store())], value=Constant(value=1)), While(test=Constant(value=True), body=[Assign(targets=[Name(id='result', ctx=Store())], value=Call(func=Attribute(value=Name(id='subprocess', ctx=Load()), attr='run', ctx=Load()), args=[Call(func=Attribute(value=Constant(value=' '), attr='join', ctx=Load()), args=[List(elts=[Constant(value='gh'), Constant(value='api'), Constant(value='-H'), Constant(value='"Accept: application/vnd.github+json"'), JoinedStr(values=[Constant(value='"https://api.github.com/orgs/tinkoff-ai/packages/container/etna%2F'), FormattedValue(value=Name(id='imag', ctx=Load()), conversion=-1), Constant(value='/versions?page='), FormattedValue(value=Name(id='page', ctx=Load()), conversion=-1), Constant(value='"')])], ctx=Load())], keywords=[])], keywords=[keyword(arg='shell', value=Constant(value=True)), keyword(arg='check', value=Constant(value=True)), keyword(arg='stdout', value=Attribute(value=Name(id='subprocess', ctx=Load()), attr='PIPE', ctx=Load()))])), Assign(targets=[Name(id='parsed_result', ctx=Store())], value=Call(func=Attribute(value=Name(id='json', ctx=Load()), attr='loads', ctx=Load()), args=[Call(func=Attribute(value=Attribute(value=Name(id='result', ctx=Load()), attr='stdout', ctx=Load()), attr='decode', ctx=Load()), args=[Constant(value='utf-8')], keywords=[])], keywords=[])), If(test=Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Name(id='parsed_result', ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Constant(value=0)]), body=[Break()], orelse=[AugAssign(target=Name(id='image__versions', ctx=Store()), op=Add(), value=Name(id='parsed_result', ctx=Load())), AugAssign(target=Name(id='page', ctx=Store()), op=Add(), value=Constant(value=1))])], orelse=[]), Assign(targets=[Name(id='image__versions', ctx=Store())], value=ListComp(elt=Name(id='image', ctx=Load()), generators=[comprehension(target=Name(id='image', ctx=Store()), iter=Name(id='image__versions', ctx=Load()), ifs=[Compare(left=Call(func=Name(id='len', ctx=Load()), args=[Subscript(value=Subscript(value=Subscript(value=Name(id='image', ctx=Load()), slice=Constant(value='metadata'), ctx=Load()), slice=Constant(value='container'), ctx=Load()), slice=Constant(value='tags'), ctx=Load())], keywords=[]), ops=[Eq()], comparators=[Constant(value=0)])], is_async=0)])), Return(value=Name(id='image__versions', ctx=Load()))], decorator_list=[]), FunctionDef(name='get_list_to_remove', args=arguments(posonlyargs=[], args=[arg(arg='leave_last_n_imag', annotation=Name(id='intV', ctx=Load())), arg(arg='image__versions', annotation=Name(id='list', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value=' Ĺ   ˙ɂƳ   g  ʹ')), Assign(targets=[Name(id='image__versions', ctx=Store())], value=Call(func=Name(id='SORTED', ctx=Load()), args=[Name(id='image__versions', ctx=Load())], keywords=[keyword(arg='key', value=Lambda(args=arguments(posonlyargs=[], args=[arg(arg='x')], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Attribute(value=Attribute(value=Name(id='datetime', ctx=Load()), attr='datetime', ctx=Load()), attr='strptime', ctx=Load()), args=[Subscript(value=Name(id='x', ctx=Load()), slice=Constant(value='created_at'), ctx=Load()), Constant(value='%Y-%m-%dT%H:%M:%SZ')], keywords=[])))])), Return(value=Subscript(value=Name(id='image__versions', ctx=Load()), slice=Slice(upper=UnaryOp(op=USub(), operand=Name(id='leave_last_n_imag', ctx=Load()))), ctx=Load()))], decorator_list=[]), FunctionDef(name='delete_pipe', args=arguments(posonlyargs=[], args=[arg(arg='imag', annotation=Name(id='_str', ctx=Load())), arg(arg='leave_last_n_imag', annotation=Name(id='intV', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[Expr(value=Constant(value='        ')), Assign(targets=[Name(id='image__versions', ctx=Store())], value=Call(func=Name(id='get_untagged_images', ctx=Load()), args=[Name(id='imag', ctx=Load())], keywords=[])), Assign(targets=[Name(id='image_versions_to_remove', ctx=Store())], value=Call(func=Name(id='get_list_to_remove', ctx=Load()), args=[Name(id='leave_last_n_imag', ctx=Load()), Name(id='image__versions', ctx=Load())], keywords=[])), Expr(value=Call(func=Name(id='remove_images', ctx=Load()), args=[Name(id='image_versions_to_remove', ctx=Load())], keywords=[]))], decorator_list=[]), FunctionDef(name='remove_images', args=arguments(posonlyargs=[], args=[arg(arg='image__versions', annotation=Name(id='list', ctx=Load()))], kwonlyargs=[], kw_defaults=[], defaults=[]), body=[For(target=Name(id='image', ctx=Store()), iter=Name(id='image__versions', ctx=Load()), body=[Expr(value=Call(func=Name(id='printfQgA', ctx=Load()), args=[JoinedStr(values=[Constant(value='Removing '), FormattedValue(value=Subscript(value=Name(id='image', ctx=Load()), slice=Constant(value='url'), ctx=Load()), conversion=-1)])], keywords=[])), Expr(value=Call(func=Attribute(value=Name(id='subprocess', ctx=Load()), attr='run', ctx=Load()), args=[Call(func=Attribute(value=Constant(value=' '), attr='join', ctx=Load()), args=[List(elts=[Constant(value='echo -n |'), Constant(value='gh'), Constant(value='api'), Constant(value='--method'), Constant(value='DELETE'), Constant(value='-H'), Constant(value='"Accept: application/vnd.github+json"'), JoinedStr(values=[Constant(value='"'), FormattedValue(value=Subscript(value=Name(id='image', ctx=Load()), slice=Constant(value='url'), ctx=Load()), conversion=-1), Constant(value='"')]), Constant(value='--input -')], ctx=Load())], keywords=[])], keywords=[keyword(arg='shell', value=Constant(value=True)), keyword(arg='check', value=Constant(value=True))]))], orelse=[])], decorator_list=[]), If(test=Compare(left=Name(id='__name__', ctx=Load()), ops=[Eq()], comparators=[Constant(value='__main__')]), body=[Expr(value=Call(func=Name(id='delete_pipe', ctx=Load()), args=[Constant(value='etna-cpu'), Constant(value=20)], keywords=[])), Expr(value=Call(func=Name(id='delete_pipe', ctx=Load()), args=[Constant(value='etna-cuda-10.2'), Constant(value=20)], keywords=[])), Expr(value=Call(func=Name(id='delete_pipe', ctx=Load()), args=[Constant(value='etna-cuda-11.1'), Constant(value=20)], keywords=[])), Expr(value=Call(func=Name(id='delete_pipe', ctx=Load()), args=[Constant(value='etna-cuda-11.6.2'), Constant(value=20)], keywords=[]))], orelse=[])], type_ignores=[])
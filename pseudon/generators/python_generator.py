from pseudon.code_generator import CodeGenerator


class PythonGenerator(CodeGenerator):
    '''Python code generator'''

    def body(self, node, indent):
        if node.body:
            return self.render_nodes(node.body, indent)
        else:
            return '%spass\n' % self.offset(indent)

    def methods(self, node, indent):
        if node.methods:
            return self.render_nodes(node.methods, indent)
        else:
            return '%spass\n' % self.offset(indent)

    def safe_single(self, node, indent):
        if "'" in node.value:
            if '"' in node.value:
                s = "'%s'" % node.value.replace("'", "\'")
            else:
                s = '"%s"' % node.value
        else:
            s = "'%s'" % node.value
        return '%s%s' % (self.offset(indent), s)

    def to_boolean(self, node, indent):
        if 
    templates = {
        'module': "%<code>",

        'function': '''
                    def %<name>(%<args:join ','>):
                        %<#body>
                    ''',

        'class':  '''
                  class %<name>%?<(%<parent>)>:
                      %<#methods>
                  ''',

        'name': '%<label>',
        'int': '%<value>',
        'float': '%<value>',
        'string': safe_single,
        'boolean': to_boolean,
        'null':   'None'
    }

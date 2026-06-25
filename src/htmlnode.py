class HTMLNode():
    def __init__(self, tag: str | None = None, value: str | None = None, children: list["HTMLNode"] | None = None, props: dict[str,str] | None = None):
        self.tag = tag
        self.value = value
        self.children  = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        formatted_string = ""
        if not self.props:
            return formatted_string
        for key, value in self.props.items():
            formatted_string+= f' {key}="{value}"'
        return formatted_string
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"  #added children to see from solution
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = None, props: dict[str,str] | None = None):
        super().__init__(tag,value,None,props) #added None and props after seeing solution and talking to boots on why.
        # self.props = props # after seeing solution, i can just super children to None instead of overriding props
    
    # def props_to_html(self): #redundant and un needed, it already inhertis this from parent.
    #     return super().props_to_html()
    
    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("No value, leaf node must have a value")
        if self.tag is None:
            return self.value
        # if self.props is not None: this is not needed as propstohtml returns an empty string if propsis none.
        #     props_string = self.props_to_html()
        #     return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"  #added self.props to html after the fact to match with solution
    
    def __repr__(self) -> str:
        return f"LeafNode(tag : {self.tag}, value: {self.value}, props : {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag: str = None, children: list["HTMLNode"] = None, props: dict[str,str] | None = None):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:  #added -> str after seeing solution
        if self.tag is None:
            raise ValueError("this parent node has no tag, tag is required")
        if self.children is None:
            raise ValueError("This ParentNode has no children, children are required")
        html_string = ""
        for child in self.children:
            html_string += child.to_html()
        return f"<{self.tag}>{html_string}</{self.tag}>"

    def __repr__(self) -> str: #copied from solution as i forgot to add it myself.
        return f"ParentNode(tag : {self.tag}, children: {self.children}, props : {self.props})"
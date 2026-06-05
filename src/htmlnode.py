class HTMLNode():
    def __init__(self, tag: str | None = None, value: str | None = None, children: list["HTMLNode"] | None = None, props: dict | None = None):
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
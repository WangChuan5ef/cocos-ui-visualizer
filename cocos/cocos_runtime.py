#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cocos Runtime Module
Handles rendering and runtime visualization of Cocos UI elements
"""

from typing import Dict, Any, Optional, List, Tuple
from dataclasses import dataclass


@dataclass
class Color:
    """Color representation"""
    r: int = 255
    g: int = 255
    b: int = 255
    a: int = 255
    
    def to_tuple(self) -> Tuple[int, int, int, int]:
        """Convert to RGBA tuple"""
        return (self.r, self.g, self.b, self.a)


@dataclass
class Transform:
    """Transform properties for nodes"""
    x: float = 0.0
    y: float = 0.0
    scale_x: float = 1.0
    scale_y: float = 1.0
    rotation: float = 0.0
    opacity: int = 255


class CocosNode:
    """Represents a Cocos node in the scene tree"""
    
    def __init__(self, name: str, node_type: str, data: Optional[Dict[str, Any]] = None):
        """
        Initialize a Cocos node
        
        Args:
            name: Node name
            node_type: Type of node (e.g., 'Panel', 'Button', 'Label')
            data: Node data dictionary
        """
        self.name = name
        self.type = node_type
        self.data = data or {}
        self.children: List['CocosNode'] = []
        self.parent: Optional['CocosNode'] = None
        self.transform = Transform()
        self.color = Color()
        self.visible = True
        self.properties = {}
        
    def add_child(self, child: 'CocosNode') -> None:
        """Add a child node"""
        self.children.append(child)
        child.parent = self
        
    def remove_child(self, child: 'CocosNode') -> None:
        """Remove a child node"""
        if child in self.children:
            self.children.remove(child)
            child.parent = None
            
    def get_hierarchy_string(self, indent: int = 0) -> str:
        """Get a string representation of the node hierarchy"""
        result = "  " * indent + f"[{self.type}] {self.name}\n"
        for child in self.children:
            result += child.get_hierarchy_string(indent + 1)
        return result
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert node to dictionary"""
        return {
            "name": self.name,
            "type": self.type,
            "visible": self.visible,
            "transform": {
                "x": self.transform.x,
                "y": self.transform.y,
                "scale_x": self.transform.scale_x,
                "scale_y": self.transform.scale_y,
                "rotation": self.transform.rotation,
                "opacity": self.transform.opacity,
            },
            "color": {
                "r": self.color.r,
                "g": self.color.g,
                "b": self.color.b,
                "a": self.color.a,
            },
            "properties": self.properties,
            "children": [child.to_dict() for child in self.children],
        }


class CocosRuntime:
    """Runtime engine for Cocos UI visualization"""
    
    def __init__(self):
        """Initialize the runtime engine"""
        self.root_node: Optional[CocosNode] = None
        self.nodes_map: Dict[str, CocosNode] = {}
        self.animations = {}
        self.resources = {}
        self.show_hidden = False
        self.panel_fill = True
        
    def create_node(self, name: str, node_type: str, 
                   data: Optional[Dict[str, Any]] = None) -> CocosNode:
        """Create a new node"""
        node = CocosNode(name, node_type, data)
        self.nodes_map[name] = node
        return node
    
    def set_root_node(self, node: CocosNode) -> None:
        """Set the root node of the scene"""
        self.root_node = node
        
    def get_all_nodes(self) -> List[CocosNode]:
        """Get all nodes in the scene"""
        result = []
        
        def traverse(node):
            result.append(node)
            for child in node.children:
                traverse(child)
        
        if self.root_node:
            traverse(self.root_node)
        
        return result
    
    def set_node_property(self, node_name: str, key: str, value: Any) -> bool:
        """Set a property on a node"""
        if node_name not in self.nodes_map:
            return False
        
        node = self.nodes_map[node_name]
        node.properties[key] = value
        return True
    
    def get_node_info(self, node_name: str) -> Optional[Dict[str, Any]]:
        """Get information about a node"""
        if node_name not in self.nodes_map:
            return None
        
        node = self.nodes_map[node_name]
        return {
            "name": node.name,
            "type": node.type,
            "visible": node.visible,
            "position": (node.transform.x, node.transform.y),
            "scale": (node.transform.scale_x, node.transform.scale_y),
            "rotation": node.transform.rotation,
            "opacity": node.transform.opacity,
            "color": node.color.to_tuple(),
            "children_count": len(node.children),
            "properties": node.properties,
        }
    
    def toggle_show_hidden(self) -> None:
        """Toggle the show hidden nodes setting"""
        self.show_hidden = not self.show_hidden
        
    def toggle_panel_fill(self) -> None:
        """Toggle the panel fill setting"""
        self.panel_fill = not self.panel_fill
    
    def get_visible_nodes(self) -> List[CocosNode]:
        """Get all visible nodes based on current settings"""
        all_nodes = self.get_all_nodes()
        
        if self.show_hidden:
            return all_nodes
        
        return [node for node in all_nodes if node.visible]
    
    def register_resource(self, resource_name: str, resource_path: str) -> None:
        """Register a resource"""
        self.resources[resource_name] = resource_path
        
    def validate_resources(self) -> Dict[str, Any]:
        """Validate all resources"""
        result = {
            "total": len(self.resources),
            "valid": 0,
            "missing": [],
        }
        
        for name, path in self.resources.items():
            # In a real implementation, check if file exists
            from pathlib import Path
            if Path(path).exists():
                result["valid"] += 1
            else:
                result["missing"].append(name)
        
        return result
    
    def get_scene_info(self) -> Dict[str, Any]:
        """Get information about the entire scene"""
        return {
            "total_nodes": len(self.get_all_nodes()),
            "visible_nodes": len(self.get_visible_nodes()),
            "total_resources": len(self.resources),
            "show_hidden": self.show_hidden,
            "panel_fill": self.panel_fill,
        }

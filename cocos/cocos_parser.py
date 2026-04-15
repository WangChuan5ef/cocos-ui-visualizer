#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cocos Parser Module
Handles parsing of .csb and .json UI files
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional, Union


class CocosParser:
    """Parser for Cocos UI files"""
    
    def __init__(self):
        """Initialize the parser"""
        self.data = None
        self.file_path = None
        
    def parse_file(self, file_path: Union[str, Path]) -> Optional[Dict[str, Any]]:
        """
        Parse a Cocos UI file
        
        Args:
            file_path: Path to the .csb or .json file
            
        Returns:
            Parsed data as dictionary, or None if parsing failed
        """
        file_path = Path(file_path)
        
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        if file_path.suffix.lower() == '.json':
            return self._parse_json(file_path)
        elif file_path.suffix.lower() == '.csb':
            return self._parse_csb(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_path.suffix}")
    
    def _parse_json(self, file_path: Path) -> Dict[str, Any]:
        """Parse a JSON UI file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.data = json.load(f)
                self.file_path = file_path
                return self.data
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON file: {e}")
        except Exception as e:
            raise Exception(f"Error parsing JSON: {e}")
    
    def _parse_csb(self, file_path: Path) -> Dict[str, Any]:
        """
        Parse a CSB (Cocos Scene Binary) file
        
        Note: CSB is a binary format. This is a placeholder for binary parsing.
        In a complete implementation, this would decode the binary format.
        """
        try:
            # This is a placeholder for CSB parsing
            # In production, you would implement proper binary parsing here
            with open(file_path, 'rb') as f:
                binary_data = f.read()
            
            self.file_path = file_path
            # TODO: Implement actual CSB binary parsing
            # For now, return placeholder data
            return {
                "format": "csb",
                "file": str(file_path),
                "size": len(binary_data),
                "nodes": []
            }
        except Exception as e:
            raise Exception(f"Error parsing CSB file: {e}")
    
    def get_nodes(self) -> list:
        """Get all nodes from parsed data"""
        if self.data is None:
            return []
        
        if isinstance(self.data, dict):
            return self.data.get('nodes', [])
        return []
    
    def get_node_by_id(self, node_id: str) -> Optional[Dict[str, Any]]:
        """Get a specific node by ID"""
        nodes = self.get_nodes()
        
        def find_node(node_list, target_id):
            for node in node_list:
                if node.get('id') == target_id or node.get('name') == target_id:
                    return node
                # Search in children
                children = node.get('children', [])
                if children:
                    result = find_node(children, target_id)
                    if result:
                        return result
            return None
        
        return find_node(nodes, node_id)
    
    def get_file_info(self) -> Dict[str, Any]:
        """Get information about the parsed file"""
        return {
            "file_path": str(self.file_path),
            "file_name": self.file_path.name if self.file_path else None,
            "file_size": self.file_path.stat().st_size if self.file_path else None,
            "node_count": len(self.get_nodes()),
        }

#!/usr/bin/env python3
"""
Validation script for 60s Skills
Validates JSON format and checks skill definitions
"""

import json
import os
import sys
from pathlib import Path

def validate_json_file(file_path):
    """Validate a JSON file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json.load(f)
        return True, None
    except json.JSONDecodeError as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)

def validate_mcp_skill(skill_data, file_path):
    """Validate MCP skill structure"""
    required_fields = ['name', 'version', 'description', 'protocol', 'tools', 'metadata']
    missing = [field for field in required_fields if field not in skill_data]
    
    if missing:
        return False, f"Missing required fields: {', '.join(missing)}"
    
    if skill_data.get('protocol') != 'mcp':
        return False, f"Protocol must be 'mcp', got '{skill_data.get('protocol')}'"
    
    # Validate tools
    if not isinstance(skill_data.get('tools'), list):
        return False, "Tools must be a list"
    
    for i, tool in enumerate(skill_data['tools']):
        tool_required = ['name', 'description', 'inputSchema', 'endpoint']
        tool_missing = [field for field in tool_required if field not in tool]
        if tool_missing:
            return False, f"Tool {i}: missing fields {', '.join(tool_missing)}"
    
    return True, None

def validate_openai_skill(skill_data, file_path):
    """Validate OpenAI skill structure"""
    required_fields = ['openapi', 'info', 'servers', 'paths']
    missing = [field for field in required_fields if field not in skill_data]
    
    if missing:
        return False, f"Missing required fields: {', '.join(missing)}"
    
    return True, None

def main():
    """Main validation function"""
    print("🔍 Validating 60s Skills...")
    print()
    
    project_root = Path(__file__).parent.parent
    skills_dir = project_root / 'skills'
    
    errors = []
    success_count = 0
    total_count = 0
    
    # Validate all JSON files
    for json_file in skills_dir.rglob('*.json'):
        total_count += 1
        rel_path = json_file.relative_to(project_root)
        
        # Validate JSON format
        valid, error = validate_json_file(json_file)
        if not valid:
            errors.append(f"❌ {rel_path}: JSON parsing error - {error}")
            continue
        
        # Load and validate structure
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Validate based on type
        if 'mcp' in str(json_file) and json_file.name != 'index.json':
            valid, error = validate_mcp_skill(data, json_file)
            if not valid:
                errors.append(f"❌ {rel_path}: MCP validation error - {error}")
                continue
        
        elif 'openai' in str(json_file):
            valid, error = validate_openai_skill(data, json_file)
            if not valid:
                errors.append(f"❌ {rel_path}: OpenAPI validation error - {error}")
                continue
        
        print(f"✅ {rel_path}")
        success_count += 1
    
    print()
    print(f"📊 Results: {success_count}/{total_count} files validated successfully")
    
    if errors:
        print()
        print("❌ Errors found:")
        for error in errors:
            print(f"  {error}")
        return 1
    
    print()
    print("🎉 All validations passed!")
    return 0

if __name__ == '__main__':
    sys.exit(main())

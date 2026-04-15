/*
 * Cocos Scene Binary Format Definitions
 * 
 * This header file contains the binary format structures for
 * parsing .csb (Cocos Scene Binary) files.
 * 
 * Generated for: Cocos2d-x UI Visualization Tool
 */

#ifndef __CSPARSEBINARY_GENERATED_H__
#define __CSPARSEBINARY_GENERATED_H__

#include <stdint.h>
#include <string>
#include <vector>
#include <map>

namespace cocos2d {
namespace cocostudio {

/**
 * Binary Format Version Information
 */
#define CSB_VERSION_MAJOR 1
#define CSB_VERSION_MINOR 0
#define CSB_FORMAT_VERSION "1.0.0"

/**
 * Binary Data Type Definitions
 */
typedef uint8_t   byte;
typedef uint16_t  word;
typedef uint32_t  dword;
typedef int16_t   short_t;
typedef int32_t   int_t;
typedef float     float_t;

/**
 * CSB File Header Structure
 */
struct CSBHeader {
    byte   signature[4];      // "CCSB" magic number
    dword  version;           // File format version
    dword  header_length;     // Header size in bytes
    dword  data_length;       // Data section size
    dword  reserved;          // Reserved for future use
};

/**
 * Node Type Definitions
 */
enum class NodeType : uint16_t {
    UNKNOWN         = 0,
    SPRITE          = 1,
    PANEL           = 2,
    BUTTON          = 3,
    CHECK_BOX       = 4,
    IMAGE_VIEW      = 5,
    TEXT_BUTTON     = 6,
    LABEL           = 7,
    LAYOUT          = 8,
    SCROLL_VIEW     = 9,
    LIST_VIEW       = 10,
    PAGE_VIEW       = 11,
    SLIDER          = 12,
    TEXT_FIELD      = 13,
    BONE            = 14,
    ARMATURE        = 15,
    PARTICLE        = 16,
    CUSTOM_NODE     = 17,
    PROJECT_NODE    = 18,
    COMPONENT       = 19
};

/**
 * Property Type Definitions
 */
enum class PropertyType : byte {
    PROP_NONE           = 0,
    PROP_BOOL           = 1,
    PROP_INT            = 2,
    PROP_FLOAT          = 3,
    PROP_STRING         = 4,
    PROP_VECTOR2        = 5,
    PROP_VECTOR3        = 6,
    PROP_COLOR3         = 7,
    PROP_COLOR4         = 8,
    PROP_RESOURCE       = 9,
    PROP_RECT           = 10,
    PROP_QUATERNION     = 11,
    PROP_MATRIX         = 12,
    PROP_SIZE           = 13,
    PROP_ANCHOR_POINT   = 14,
    PROP_POSITION       = 15,
    PROP_SCALE          = 16,
    PROP_ROTATION       = 17,
    PROP_SKEW           = 18,
    PROP_OPACITY        = 19
};

/**
 * Node Property Structure
 */
struct NodeProperty {
    char        name[64];          // Property name
    PropertyType type;             // Property type
    byte        reserved;
    dword       data_offset;       // Offset to property data
    dword       data_size;         // Size of property data
};

/**
 * Node Structure
 */
struct Node {
    uint16_t    node_id;           // Unique node identifier
    uint16_t    node_type;         // Type of node
    char        node_name[64];     // Node name
    
    // Transform data
    float       position_x;
    float       position_y;
    float       scale_x;
    float       scale_y;
    float       rotation;
    float       skew_x;
    float       skew_y;
    
    // Appearance
    uint8_t     opacity;
    uint8_t     color_r;
    uint8_t     color_g;
    uint8_t     color_b;
    
    // Node properties
    uint16_t    property_count;
    uint16_t    child_count;
    
    byte        visible;           // Visibility flag
    byte        touch_enabled;     // Touch input enabled
    
    dword       properties_offset; // Offset to property data
    dword       children_offset;   // Offset to child nodes
};

/**
 * Resource Reference Structure
 */
struct ResourceRef {
    char        type[32];          // Resource type (texture, sound, etc.)
    char        path[256];         // Resource file path
    dword       resource_id;       // Resource identifier
};

/**
 * Animation Key Frame Structure
 */
struct KeyFrame {
    uint16_t    frame_index;
    uint16_t    frame_type;        // Tween type
    float       value_f;           // Float value
    dword       value_i;           // Integer value
    char        value_s[64];       // String value
};

/**
 * Animation Track Structure
 */
struct AnimationTrack {
    char        track_name[64];    // Animation track name
    uint16_t    property_type;     // Property being animated
    uint16_t    keyframe_count;
    dword       keyframe_offset;   // Offset to keyframes
};

/**
 * Animation Structure
 */
struct Animation {
    char        animation_name[64];    // Animation name
    uint16_t    track_count;           // Number of animation tracks
    uint16_t    frame_count;           // Total frames
    float       duration;              // Duration in seconds
    dword       track_offset;          // Offset to animation tracks
};

/**
 * Scene Structure
 */
struct Scene {
    char        scene_name[64];     // Scene identifier
    uint16_t    node_count;         // Total nodes in scene
    uint16_t    animation_count;    // Total animations
    dword       nodes_offset;       // Offset to root node
    dword       animations_offset;  // Offset to animations
};

/**
 * Binary File Structure
 */
struct CSBFile {
    CSBHeader   header;             // File header
    Scene       scene;              // Scene data
    // Additional data sections follow based on offsets
};

/**
 * Helper functions for binary parsing
 */
inline bool IsValidCSBSignature(const byte* signature) {
    return signature[0] == 'C' &&
           signature[1] == 'C' &&
           signature[2] == 'S' &&
           signature[3] == 'B';
}

inline bool IsCompatibleVersion(dword version) {
    uint16_t major = (version >> 16) & 0xFFFF;
    uint16_t minor = version & 0xFFFF;
    return major == CSB_VERSION_MAJOR && minor <= CSB_VERSION_MINOR;
}

} // namespace cocostudio
} // namespace cocos2d

#endif // __CSPARSEBINARY_GENERATED_H__

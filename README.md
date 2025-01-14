# Custom Desktop Mate (.VRM) Creation

This guide provides a step-by-step process for creating a custom Desktop Mate using the .vrm file format. The process involves creating a 3D model, importing it into Unity, adding animations and interactions through coding, and exporting it as a .vrm file for use in desktop mascot applications.

---

## 🚀 Overview
A **Desktop Mate** is a virtual desktop mascot that interacts with users. The **.vrm file format** is commonly used for virtual avatars and is compatible with various desktop applications like **VSeeFace** and **Desktop Mascot Engine**.

The creation process includes:
1. Creating a 3D model.
2. Importing it into Unity.
3. Coding custom interactions.
4. Exporting it as a .vrm file.

---

## 🎨 Step 1: Create Your 3D Model

### Option 1: Using VRoid Studio (Beginner-Friendly)
- Download VRoid Studio: [https://vroid.com/en/studio](https://vroid.com/en/studio)
- Customize your avatar.
- Export the model as a .vrm file.

### Option 2: Using Blender (Advanced)
- Download Blender: [https://www.blender.org/](https://www.blender.org/)
- Install the Cats Blender Plugin: [https://github.com/GiveMeAllYourCats/cats-blender-plugin](https://github.com/GiveMeAllYourCats/cats-blender-plugin)
- Create or import a 3D model.
- Convert the model to the .vrm format using the plugin.

---

## ⚙️ Step 2: Import Your Model into Unity

1. Download and install **Unity Hub**: [https://unity.com/download](https://unity.com/download)
2. Install the **UniVRM Plugin**: [https://github.com/vrm-c/UniVRM](https://github.com/vrm-c/UniVRM)
3. Open Unity and create a new project.
4. Import your **.vrm file** into Unity.

---

## 💻 Step 3: Code Custom Interactions (C#)

To make your Desktop Mate interactive, write C# scripts in Unity.

### Example: Waving Animation Script
```csharp
using UnityEngine;

public class DesktopMate : MonoBehaviour
{
    public Animator animator;

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.W))
        {
            animator.SetTrigger("Wave");
        }
    }
}
```

---

## 📦 Step 4: Export Your Custom Desktop Mate

1. Once your model and scripts are ready, go to **VRM → Export to .VRM**.
2. Save your file as **YourMate.vrm**.

---

## 🎯 Step 5: Use a Desktop Mate App

To load and use your custom **Desktop Mate**, you can use the following apps:

- **VSeeFace**: [https://www.vseeface.icu/](https://www.vseeface.icu/)
- **Luppet**: [https://luppet.app/](https://luppet.app/)
- **Desktop Mascot Engine**: [https://desktop-mascot.com/](https://desktop-mascot.com/)

---

## 🔧 Optional: Adding AI Interaction
For a more advanced Desktop Mate, you can integrate **AI interaction** using:
- **ChatGPT API** for chatbot functionality.
- **Unity ML-Agents** for advanced behaviors.

---

## 📚 Tools & Resources
| Tool             | Purpose                 | Link                                |
|------------------|-------------------------|-------------------------------------|
| Unity            | Game Engine             | [https://unity.com/download](https://unity.com/download) |
| UniVRM Plugin    | VRM Support for Unity   | [https://github.com/vrm-c/UniVRM](https://github.com/vrm-c/UniVRM) |
| Blender          | 3D Modeling             | [https://www.blender.org/](https://www.blender.org/) |
| VRoid Studio     | Avatar Creation         | [https://vroid.com/en/studio](https://vroid.com/en/studio) |
| Cats Plugin      | Blender to VRM Export   | [https://github.com/GiveMeAllYourCats/cats-blender-plugin](https://github.com/GiveMeAllYourCats/cats-blender-plugin) |

---

## 🛠️ Future Development
- Implement voice commands.
- Add more animations.
- Use AI for smart responses.

---

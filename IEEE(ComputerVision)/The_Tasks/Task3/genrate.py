

os.makedirs("folders")
os.chdir(r'E:\Ai\CV\session 4\task\folders')
for i in range(5):
    os.makedirs(f"folder{i+1}")

x = 1
for folder_name in os.listdir(r'E:\Ai\CV\session 4\task\folders') :
    imgs = cv2.imread(fr'E:\Ai\CV\session 4\task\images\{x}.jpg')
    x = x + 1
    path = fr"E:\Ai\CV\session 4\task\folders\{folder_name}"
    os.chdir(path)
    for i in range(50):
        cv2.imwrite(f"{i+1}.jpg", imgs)

print(" complete.")

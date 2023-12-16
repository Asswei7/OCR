import os
import shutil
from tqdm import tqdm
# 删除相似的图片
# 原理：将图片变成哈希码，对哈希码进行比较
# 精度不够准确，很多不一样的图片识别成同一张图片
# 解决方法，先读取图片的文字，如果文字
if __name__=='__main__':
    from imagededup.methods import PHash
    phasher = PHash()
    new_img_path = r"/video/extract_result"  # 要处理的文件路径
    merge = r"E:\Habei\TestImport\video\m2"  # 合并后路径（是一个空文件夹路径，取用存放去重后不重复的图片）
    new_dataset_duplicates = phasher.find_duplicates(image_dir=new_img_path)
    print(new_dataset_duplicates)
    new_k = []
    new_v = []
    for k, v in tqdm(new_dataset_duplicates.items(), desc="筛选新数据集"):
        '''其实没必要搞这么麻烦，主要是防止出现类似 1：[], 2：[3, 1]或者 
        2：[3, 1], 1：[]的情况，但会大大增加计算量，要求不大的话一层for循环就能搞定'''
        if len(v) == 0 and (k not in new_v):
            new_k.append(k)
            new_v.extend(v)
            continue
        if k not in new_v:
            if len(new_k) == 0:
                new_k.append(k)
                new_v.extend(v)
                continue
            for jug in new_k:
                if jug in v:
                    break
                else:
                    new_k.append(k)
                    new_v.extend(v)
                    break
    # 将新数据集中不重复的数据迁移到另一个文件夹中
    for q in tqdm(new_k, desc='迁移不重复新数据集'):
        local = os.path.join(new_img_path, q)
        shutil.copy(local, merge)

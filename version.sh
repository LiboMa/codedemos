#!/bin/bash

BIG_VERSION=4.0.0
# 获取当前Git分支名称

BRANCH_NAME=$(git rev-parse --abbrev-ref HEAD)

# 替换分支名称中的特殊字符（例如'/'转换为'-'）
BRANCH_NAME=$(echo "${BRANCH_NAME}" | sed 's/\//\-/g')

# 获取最近的Git commit hash
COMMIT_HASH=$(git rev-parse --short HEAD)

# 生成镜像tag
IMAGE_TAG="${BRANCH_NAME}-${COMMIT_HASH}"

# 构建和推送Docker镜像的步骤与之前相同，只是使用IMAGE_TAG作为tag

echo "$BIG_VERSION-$IMAGE_TAG"
